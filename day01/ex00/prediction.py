import numpy as np

def predict_(x, theta):
    x = np.array([(1., xi) for xi in x])
    return np.dot(x, theta)
