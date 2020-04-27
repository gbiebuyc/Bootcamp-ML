#!/usr/bin/env python3
from TinyStatistician import TinyStatistician

tstat = TinyStatistician()
a = [1, 42, 300, 10, 59]
print('array:', a)
print('mean:', tstat.mean(a))
print('median:', tstat.median(a))
print('quartile 25:', tstat.quartiles(a, 25))
print('quartile 75:', tstat.quartiles(a, 75))
print('variance:', tstat.var(a))
print('standard deviation:', tstat.std(a))
