#!/usr/bin/env python3
import numpy as np
from cost import cost_

X = np.array([0, 15, -9, 7, 12, 3, -21])
Y = np.array([2, 14, -13, 5, 12, 4, -19])

# Example 1:
output = cost_(X, Y)
print(output)
assert output == 4.285714285714286

# Example 2:
output = cost_(X, X)
print(output)
assert output == 0.0
