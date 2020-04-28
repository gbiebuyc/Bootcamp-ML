import matplotlib
import matplotlib.pyplot as plt
from prediction import predict_
from vec_cost import cost_

def plot_with_cost(x, y, theta):
    y_hat = predict_(x, theta)
    cost = cost_(y, y_hat)
    plt.plot(x, y, 'bo')
    plt.plot(x, y_hat, 'r', c='orangered')
    plt.title(str(cost))
    plt.plot((x,x), (y, y_hat), '--r')
    plt.show()

