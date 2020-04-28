#!/usr/bin/env python3
from cost import cost_, cost_elem_
from prediction import predict_
import numpy as np

x1 = np.array([[0.], [1.], [2.], [3.], [4.]])
theta1 = np.array([[2.], [4.]])
y_hat1 = predict_(x1, theta1)
y1 = np.array([[2.], [7.], [12.], [17.], [22.]])

output = cost_elem_(y1, y_hat1)
print('Example 1:', output.tolist())
#assert np.array_equal(output, [[0.], [0.1], [0.4], [0.9], [1.6]])

output = cost_(y1, y_hat1)
print('Example 2:', output)

x2 = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8., 80.]])
theta2 = np.array([[0.05], [1.], [1.], [1.]])
y_hat2 = predict_(x2, theta2)
y2 = np.array([[19.], [42.], [67.], [93.]])

output = cost_elem_(y2, y_hat2)
print('Example 3:', output.tolist())

output = cost_(y2, y_hat2)
print('Example 4:', output)

x3 = np.array([0, 15, -9, 7, 12, 3, -21])
theta3 = np.array([[0.], [1.]])
y_hat3 = predict_(x3, theta3)
y3 = np.array([2, 14, -13, 5, 12, 4, -19])

output = cost_(y3, y_hat3)
print('Example 5:', output)

output = cost_(y3, y3)
print('Example 6:', output)


