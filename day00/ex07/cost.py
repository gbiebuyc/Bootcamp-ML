import numpy as np

def cost_elem_(y, y_hat):
    """
    Description:
    Calculates all the elements (1/2*M)*(y_pred - y)^2 of the cost function.
    Args:
    y: has to be an numpy.ndarray, a vector.
    y_hat: has to be an numpy.ndarray, a vector.
    Returns:
    J_elem: numpy.ndarray, a vector of dimension (number of the training examples,1).
    None if there is a dimension matching problem between X, Y or theta.
    Raises:
    This function should not raise any Exception.
    """
    #print('y_hat:', y_hat.tolist())
    #return (1/(2*len(y))) * sum([(yyy - yy)**2 for yy, yyy in zip(y, y_hat)])
    return np.array([(yyy - yy)**2 for yy, yyy in zip(y, y_hat)])

def cost_(y, y_hat):
    """
    Description:
    Calculates the value of cost function.
    Args:
    y: has to be an numpy.ndarray, a vector.
    y_hat: has to be an numpy.ndarray, a vector.
    Returns:
    J_value : has to be a float.
    None if there is a dimension matching problem between X, Y or theta.
    Raises:
    This function should not raise any Exception.
    """
    #print(type(sum(list(cost_elem_(y, y_hat)))))
    return (1/(2*len(y))) * sum(cost_elem_(y, y_hat).flatten().tolist())
