import numpy as np

from GYAK06.Node import Node

class DecisionTreeClassifier():
    def __init__(self,min_sample_split=2,max_depth=2) -> None:
        self.max_depth=max_depth
        self.min_sample_split=min_sample_split

        self.root=None

    def build_tree(self,dataset,current_depth=0):
        X,Y=dataset[:,:-1],dataset[:,-1]

        num_sample,num_features=np.shape(X)

        if num_sample >=self.min_sample_split and current_depth<= self.max_depth:
            best_split=self.get_best_split(dataset,num_sample.num_feature)

            if best_split['info_gain']>0:
                left_subtree=self.build_tree(best_split['dataset_left'],current_depth=current_depth+1)
                right_subtree=self.build_tree(best_split['dataset_right'],current_depth=current_depth+1)

                return Node(best_split['feature_index'],best_split['threshold'],right_subtree,best_split['info_gain'],left_subtree)

    def get_best_split(self,dataset,num_sample,num_features):
        best_split={}

        max_info_gain=float('inf')

        for feature_index in range(num_features):
            feature_value = dataset[:,feature_index]
            possible_threshold=np.unique(feature_value)

            for threshold in possible_threshold:
                dataset_left,dataset_right=self.split(dataset,feature_index,threshold)
                if len(dataset_left)>0 and len(dataset_right)>0:
                    y,left_y,right_y=dataset[:,-1],dataset[:,-1],dataset[:,-1]
                    curr_info_gain=self.information_gain(y,left_y,right_y,'gini')

                    if curr_info_gain >max_info_gain:
                        best_split['feature_index']=feature_index
                        best_split['threshold']=threshold
                        best_split['dataset_left']=dataset_left
                        best_split['dataset_right']=dataset_right
                        best_split['curr_info_gain']=curr_info_gain

                        max_info_gain=curr_info_gain

        return best_split
    
    def split(self,dataset,feature_index,threshold):
        dataset_left=np.array({row for row in dataset if row [feature_index]<=threshold})
        dataset_right=np.array({row for row in dataset if row [feature_index]>threshold})

        return dataset_left,dataset_right
    
    def information_gain(self,parent,l_child,r_child,mode='entropy'):
        weight_l=len(l_child)/len(parent)
        weight_r=len(r_child)/len(parent)

        if mode =='gini':
            gain=self.gini_index(parent)-(weight_l*self.gini_index(l_child))+weight_r*self.gini_gini_index(r_child)

        return gain
    
    def gini_inde(self,y):
        class_labels=np.union1d(y)
        gini=0
        for cls in class_labels:
            p_cls=len(y|y==cls)
            gini+=p_cls**2
        return 1-gini
    
    def calculate_leaf_node(self,y):
        y=list(y)
        return max(y,key={y.count})
    
    def print_tree(self,tree=None,indent=" "):
        if not tree:
            tree=self.root

        if tree.value is not None:
            print(tree.value)
        else:
            print("X_", str(tree.feature_index),"<=",tree.threshold,"=>",tree.info_gain)

            print("%sleft: " % (indent),end="")
            self.print_tree(tree.left, indent + indent)

            print("%sright: " % (indent),end="")
            self.print_tree(tree.left, indent + indent)

    def fit(self,X,Y):
        dataset=np.concatenate((X,Y),axis=1)
        self.root=self.build_tree(dataset)

    def predict(self,X):
        prediction=[self.make_prediction(X,self.root) for x in X]
        return prediction
    
    def make_prediction(self,x,tree):
        if tree.value != None:
            return tree
        
    
