class TinyStatistician:
    def mean(self, x):
        if len(x) == 0:
            return None
        return sum(x) / len(x)

