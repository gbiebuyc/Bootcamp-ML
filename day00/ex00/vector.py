class Vector:
    def __init__(self, arg):
        if type(arg) == list:
            self.values = arg
            self.size = len(arg)
        elif type(arg) == int:
            self.values = list(range(arg))
            self.size = arg
        elif type(arg) == tuple and len(arg) <= 3:
            self.values = list(range(*arg))
            self.size = len(self.values)

    def __add__(self, other):
        if type(other) in (int, float):
            return Vector([x+other for x in self.values])
        if type(other) is Vector:
            if other.size != self.size:
                raise ValueError("Vector sizes don't match")
            return Vector([x + y for x, y in zip(self.values, other.values)])

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return self + other * -1

    def __rsub__(self, other):
        return self - other

    def __mul__(self, other):
        if type(other) in (int, float):
            return Vector([x*other for x in self.values])
        if type(other) is Vector:
            if other.size != self.size:
                raise ValueError("Vector sizes don't match")
            dot_prod = 0
            for x, y in zip(self.values, other.values):
                dot_prod += x * y
            return dot_prod

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if type(other) in (int, float):
            return Vector([x/other for x in self.values])
        raise TypeError('Vector division is only for scalars')

    def __rtruediv__(self, other):
        return self / other

    def __str__(self):
        return '(Vector %s)' % str(self.values)

    def __repr__(self):
        return '(Vector %s)' % str(self.values)
