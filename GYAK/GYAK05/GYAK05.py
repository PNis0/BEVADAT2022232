
import numpy as np
import seaborn as sns
from typing import Tuple
from scipy.stats import mode
from sklearn.metrics import confusion_matrix


# csv_path = './archive/iris.csv'


class KNNClassifier:
    
    def __init__(self, k:int, test_split_ratio:float):
        self.k = k
        self.test_split_ratio = test_split_ratio
        self.x_train = None
        self.y_train = None
        self.x_test = None
        self.y_test = None

    @property
    def k_neighbors(self):
        return self.k
    
    @staticmethod
    def load_csv(self, csv_path:str) -> Tuple[np.ndarray, np.ndarray]:
        np.random.seed(42)
        dataset = np.genfromtxt(csv_path, delimiter=',')
        np.random.shuffle(dataset)
        x, y = dataset[:,:4], dataset[:,-1]
        x[np.isnan(x)] = 3.5
        x = np.delete(x, np.where(np.logical_or(x > 13.0, x < 0.0))[0], axis=0)
        y = np.delete(y, np.where(np.logical_or(x > 13.0, x < 0.0))[0], axis=0)
        self.train_test_split(x, y)
        
    
    def train_test_split(self, features: np.ndarray, labels: np.ndarray) -> None:
        test_size = int(len(features) * self.test_split_ratio)
        train_size = len(features) - test_size
        assert len(features) == test_size + train_size, "Size mismatch!"

        self.x_train, self.y_train = features[:train_size, :], labels[:train_size]
        self.x_test, self.y_test = features[train_size:train_size + test_size, :], labels[train_size:train_size + test_size]


    def euclidean(self, element_of_x: np.ndarray) -> np.ndarray:
        return np.sqrt(np.sum((self.x_train - element_of_x) ** 2, axis=1))

    def predict(self):
        self.y_preds = []
        for element_of_x in self.x_test:
            distances = self.euclidean(element_of_x)
            sorted_distances_indices = np.argsort(distances)
            k_nearest_labels = self.y_train[sorted_distances_indices[:self.k]]
            most_common_label = np.argmax(np.bincount(k_nearest_labels.astype(int)))
            self.y_preds.append(most_common_label)
        return self.y_preds

    def accuracy(self):
        correct_predictions = np.sum(self.y_preds == self.y_test)
        accuracy = correct_predictions / len(self.y_test)
        return accuracy

    def confusion_matrix(self):
        return confusion_matrix(self.y_test, self.y_preds) 


