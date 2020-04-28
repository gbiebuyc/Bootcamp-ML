import numpy as np
import math

def mse_(y, y_hat):
    return np.mean((y - y_hat)**2)

def rmse_(y, y_hat):
    return math.sqrt(np.mean((y - y_hat)**2))

def mae_(y, y_hat):
    return np.mean(np.absolute(y - y_hat))

def r2score_(y, y_hat):
    mean = np.mean(y)
    return 1 - np.sum((y - y_hat)**2)/np.sum((y - mean)**2)
