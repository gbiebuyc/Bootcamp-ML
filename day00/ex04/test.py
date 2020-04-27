#!/usr/bin/env python3
from tools import add_intercept
import numpy as np

# Example 1:
x = np.arange(1,6)
x2 = add_intercept(x)
print(x2)
assert np.array_equal(x2, [[1., 1.], [1., 2.], [1., 3.], [1., 4.], [1., 5.]])

# Example 2:
y = np.arange(1,10).reshape((3,3))
y2 = add_intercept(y)
print(y2)
assert np.array_equal(y2, [[1., 1., 2., 3.], [1., 4., 5., 6.], [1., 7., 8., 9.]])
