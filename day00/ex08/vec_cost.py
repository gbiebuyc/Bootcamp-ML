import numpy as np

def cost_(y, y_hat):
    return (1/(2*len(y)))*np.sum((y - y_hat)**2)
