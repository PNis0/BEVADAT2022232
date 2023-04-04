class Node():
    def __init__(self,feature_index = None,value=None,threshold=None,right=None,info_gain=None) -> None:
        #leaf
        self.value = value

        #dis
        self.feature_index=feature_index
        self.threshold=threshold
        self.right=right
        self.info_gain=info_gain
