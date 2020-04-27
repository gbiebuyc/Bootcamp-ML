class TinyStatistician:
    def mean(self, x):
        if len(x) == 0:
            return None
        return sum(x) / len(x)

    def median(self, x):
        n = len(x)
        if n % 2:
            return x[n//2]
        return (x[n/2-1]+x[n/2])/2

