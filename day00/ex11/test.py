#!/usr/bin/env python3
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from math import sqrt
from other_costs import *

x = np.array([0, 15, -9, 7, 12, 3, -21])
y = np.array([2, 14, -13, 5, 12, 4, -19])

# Mean squared error
output = mse_(x,y)
print('MSE:', output)
assert output == mean_squared_error(x,y)

# Root mean squared error
output = rmse_(x,y)
print('RMSE:', output)
assert output == sqrt(mean_squared_error(x,y))

# Mean absolute error
output = mae_(x,y)
print('MAE:', output)
assert output == mean_absolute_error(x,y)

# R2-score
output = r2score_(x,y)
print('R2-score:', output)
assert output == r2_score(x,y)

