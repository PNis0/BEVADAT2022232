import numpy as np


class LinearRegression:
    def __init__(self, epochs: int = 1000, lr: float = 1e-3):
        self.epochs = epochs
        self.lr = lr

    def fit(self, X: np.array, y: np.array):
        self.weights = np.zeros(X.shape[1])
        self.bias = 0
        self.cost = []

        for epoch in range(self.epochs):
            y_pred = np.dot(X, self.weights) + self.bias

            cost = np.mean((y_pred - y) ** 2)
            self.cost.append(cost)

            dw = np.dot(X.T, (y_pred - y)) / len(y)
            db = np.sum(y_pred - y) / len(y)

            self.weights -= self.lr * dw
            self.bias -= self.lr * db

        

    def predict(self, X):
        y_pred = np.dot(X, self.weights) + self.bias
        return y_pred
