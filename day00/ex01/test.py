#!/usr/bin/env python3
from matrix import Matrix

# add
m1 = Matrix([[0.0, 1.0, 2.0, 3.0],
             [0.0, 2.0, 4.0, 6.0]])
m2 = Matrix([[0.0, 1.0, 2.0, 3.0],
             [0.0, 2.0, 4.0, 6.0]])
m3 = m1 + m2
assert m3.data == [[0.0, 2.0, 4.0, 6.0], [0.0, 4.0, 8.0, 12.0]]

# sub
m1 = Matrix([[0.0, 1.0, 2.0, 3.0],
             [0.0, 2.0, 4.0, 6.0]])
m2 = Matrix([[0.0, 1.0, 2.0, 3.0],
             [0.0, 2.0, 4.0, 6.0]])
m3 = m1 - m2
assert m3.data == [[0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0]]

# mul
m1 = Matrix([[0.0, 1.0, 2.0, 3.0],
             [0.0, 2.0, 4.0, 6.0]])
m2 = Matrix([[0.0, 1.0],
             [2.0, 3.0],
             [4.0, 5.0],
             [6.0, 7.0]])
m3 = m1 * m2
assert m3.data == [[28., 34.], [56., 68.]]
m3 = m1 * 5
assert m3.data == [[0.0, 5.0, 10.0, 15.0], [0.0, 10.0, 20.0, 30.0]]
m3 = 5 * m1
assert m3.data == [[0.0, 5.0, 10.0, 15.0], [0.0, 10.0, 20.0, 30.0]]

print('All good.')
