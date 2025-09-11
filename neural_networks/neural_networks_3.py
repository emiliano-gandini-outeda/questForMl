import numpy as np

class dense_layer:
    # Initialaze weights and biases

    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.01 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
        
    def forward(self, inputs):
        # Calculate output values from inputs, weights and biases
        pass # Placeholder
    
    pass # Placeholder



