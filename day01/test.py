#!/usr/bin/env python3
import numpy as np
from prediction import predict_

x = np.arange(1,6)

#Example 1:
theta1 = np.array([5, 0])
output = predict_(x, theta1)
print(output)
assert np.array_equal(output, [5., 5., 5., 5., 5.])

#Example 2:
theta2 = np.array([0, 1])
output = predict_(x, theta2)
print(output)
assert np.array_equal(output, [1., 2., 3., 4., 5.])

#Example 3:
theta3 = np.array([5, 3])
output = predict_(x, theta3)
print(output)
assert np.array_equal(output, [ 8., 11., 14., 17., 20.])

#Example 4:
theta4 = np.array([-3, 1])
output = predict_(x, theta4)
print(output)
assert np.array_equal(output, [-2., -1., 0., 1., 2.])

