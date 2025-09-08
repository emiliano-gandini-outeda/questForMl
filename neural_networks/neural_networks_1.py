import numpy as np

inputs = [1, 2, 3, 2.5]

wheigts = [[0.342, -0.876, 0.123, 0.567],
           [-0.234, 0.789, -0.456, 0.901],
           [0.654, -0.321, 0.987, -0.543]]

biases = [2, 3, 0.5]

layer_output = np.dot(wheigts, inputs)
    
print(layer_output)