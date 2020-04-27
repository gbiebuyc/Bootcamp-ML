class Matrix:
    def __init__(self, arg):
        if type(arg) is list:
            self.data = arg
            self.shape = (len(arg), len(arg[0]))
        if type(arg) == tuple:
            if len(arg) != 2:
                raise ValueError('Shape must be a tuple (rows, columns)')
            self.data = [[0]*arg[1] for i in range(arg[0])]
            self.shape = arg

    def __add__(self, other):
        if self.shape != other.shape:
            raise ValueError('Matrices not compatible for addition.')
        R = Matrix(self.shape)
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                R.data[i][j] = self.data[i][j] + other.data[i][j]
        return R

    def __sub__(self, other):
        return self + other * -1

    def __mul__(self, other):
        if type(other) in (int, float): # scalar mul
            R = Matrix(self.shape)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    R.data[i][j] = self.data[i][j] * other
            return R
        if type(other) is Matrix:
            if self.shape[1] != other.shape[0]:
                raise ValueError('Matrices not compatible for multiplication.')
            M = self.data
            N = other.data
            R = Matrix((self.shape[0], other.shape[1]))
            for i in range(R.shape[0]):
                for j in range(R.shape[1]):
                    for k in range(self.shape[1]):
                        R.data[i][j] += M[i][k] * N[k][j]
            return R

    def __rmul__(self, other):
        return self * other

    def __str__(self):
        return '(Matrix %s)' % str(self.data)

    def __repr__(self):
        return '(Matrix %s)' % str(self.data)

