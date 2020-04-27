#!/usr/bin/env python3
from TinyStatistician import TinyStatistician

tstat = TinyStatistician()
a = [1, 42, 300, 10, 59]
print('array:', a)
print('mean:', tstat.mean(a))
