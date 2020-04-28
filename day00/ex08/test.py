#!/usr/bin/env python3
from vec_cost import cost_
import numpy as np

X = np.array([0, 15, -9, 7, 12, 3, -21])
Y = np.array([2, 14, -13, 5, 12, 4, -19])

print('Example 1:')
output = cost_(X, Y)
print(output)
#assert output == 4.285714285714286

print('Example 2:')
output = cost_(X, X)
print(output)
#assert output == 0.0
