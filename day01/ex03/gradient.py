import numpy as np
from prediction import predict_

def simple_gradient(x, y, theta):
    y_hat = predict_(x, theta)
    component0 = np.mean(y - y_hat)
    component1 = np.mean((y - y_hat) * x)
    return np.array((component0, component1))
