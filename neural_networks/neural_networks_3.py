import numpy as np

inputs = [[1, 2, 3, 2.5], [2, 5, -1, 2], [-1.5, 2.7, 3.3, -0.8]]
class dense_layer:
    # Initialaze weights and biases

    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.1 * np.random.randn(n_inputs, n_neurons) # Inputs and then neurons to avoid doing a transpose
        self.biases = np.zeros((1, n_neurons)) # Needs to be a tuple as the shape itself (1, n_neurons) needs to be passes as a single parameter
        
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

layer1 = dense_layer(4, 5)
layer2 = dense_layer(5, 2)

layer1.forward(inputs)
layer2.forward(layer1.output)

print(layer1.output)
print(layer2.output)