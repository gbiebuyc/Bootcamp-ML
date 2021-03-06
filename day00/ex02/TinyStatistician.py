import math

class TinyStatistician:
    def mean(self, x):
        if len(x) == 0:
            return None
        return sum(x) / len(x)

    def median(self, x):
        if len(x) == 0:
            return None
        x.sort()
        n = len(x)
        if n % 2:
            return x[n//2]
        return (x[n/2-1]+x[n/2])/2

    def quartiles(self, x, percentile):
        if len(x) == 0:
            return None
        return sorted(x)[int(len(x)*percentile*0.01)]

    def var(self, x):
        if len(x) == 0:
            return None
        mean = self.mean(x)
        return self.mean([(mean-y)**2 for y in x])

    def std(self, x):
        if len(x) == 0:
            return None
        return math.sqrt(self.var(x))
