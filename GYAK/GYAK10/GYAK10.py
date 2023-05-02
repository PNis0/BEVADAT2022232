import numpy as np

class ReLU():
    def forward_pass(self, x):
        return np.where(x >= 0, x, 0)

class Dense:
    """A fully-connected NN layer.
    Parameters:
    -----------
    n_output: int
        The number of neurons in the layer.
    n_input: int
        The expected input shape of the layer. For dense layers a single digit specifying
        the number of features of the input. Must be specified if it is the first layer in
        the network.
    """

    def __init__(self, n_output, n_input=None):
        self.layer_input = None
        self.n_input = n_input
        self.n_output = n_output
        # self.trainable = True
        self.W = None
        self.bias = None
        self.initialize()

    def initialize(self):
        # Initialize the weights
        np.random.seed(42)
        self.W = np.random.normal(0.0, 1, (self.n_input, self.n_output))
        self.bias = np.random.random(size=(self.n_output))

    def forward_pass_a(self, X):
       resultArray= np.matmul(X,self.W)
       return resultArray+self.bias
       pass