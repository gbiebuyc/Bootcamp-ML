import numpy as np

def gradient(x, y, theta):
    x = np.array([(1., xi) for xi in x])
    m = len(y)
    return (1/m) * np.dot(np.transpose(x), (x*theta - y))
