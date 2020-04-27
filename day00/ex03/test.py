#!/usr/bin/env python3
from prediction import simple_predict
import numpy as np

x = np.arange(1,6)

#Example 1:
theta1 = np.array([5, 0])
p = simple_predict(x, theta1)
assert np.array_equal(p, [5., 5., 5., 5., 5.])
print(p)

#Example 2:
theta2 = np.array([0, 1])
p = simple_predict(x, theta2)
assert np.array_equal(p, [1., 2., 3., 4., 5.])
print(p)

#Example 3:
theta3 = np.array([5, 3])
p = simple_predict(x, theta3)
assert np.array_equal(p, [ 8., 11., 14., 17., 20.])
print(p)

#Example 4:
theta4 = np.array([-3, 1])
p = simple_predict(x, theta4)
assert np.array_equal(p, [-2., -1., 0., 1., 2.])
print(p)
