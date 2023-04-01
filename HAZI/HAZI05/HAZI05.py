
import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix
import math


class KNNClassifier:
    def __init__(self, k):
        self.k = k
        self.X_train = None
        self.y_train = None
        self.y_preds = None

    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def euclidean_distance(self, row1, row2):
        distance = 0.0
        for i in range(len(row1)):
            distance += (row1[i] - row2[i]) ** 2
        return math.sqrt(distance)

    def predict(self, X_test):
        distances = []
        targets = []
        for i in range(len(self.X_train)):
            distance = self.euclidean_distance(self.X_train.iloc[i], X_test)
            distances.append([distance, i])
        distances.sort()
        for i in range(self.k):
            index = distances[i][1]
            targets.append(self.y_train.iloc[index])
        self.y_preds = pd.Series(targets)

    @staticmethod
    def accuracy(y_test, y_preds):
        return accuracy_score(y_test, y_preds)

    @staticmethod
    def confusion_matrix(y_test, y_preds):
        return confusion_matrix(y_test, y_preds)
        
    @property
    def k_neighbors(self):
        return self.k


