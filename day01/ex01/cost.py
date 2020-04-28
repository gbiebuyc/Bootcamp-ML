import numpy as np

def cost_(y, y_hat):
    #return (1/(2*len(y))) * np.sum((y_hat - y)**2)
    return np.mean((y_hat - y)**2)
