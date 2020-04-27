#!/usr/bin/env python3
from prediction import predict_
import numpy as np

x = np.arange(1,6)

#Example 1:
theta1 = np.array([5, 0])
p = predict_(x, theta1)
print(p)
assert np.array_equal(p, [5., 5., 5., 5., 5.])

#Example 2:
theta2 = np.array([0, 1])
p = predict_(x, theta2)
print(p)
assert np.array_equal(p, [1., 2., 3., 4., 5.])

#Example 3:
theta3 = np.array([5, 3])
p = predict_(x, theta3)
print(p)
assert np.array_equal(p, [ 8., 11., 14., 17., 20.])

#Example 4:
theta4 = np.array([-3, 1])
p = predict_(x, theta4)
print(p)
assert np.array_equal(p, [-2., -1., 0., 1., 2.])
