#!/usr/bin/env python3
from vector import Vector

# init
v1 = Vector(3) # with a size
assert v1.values == [0.0, 1.0, 2.0]
assert v1.size == 3
v1 = Vector((10,15)) # with a range
assert v1.values ==  [10.0, 11.0, 12.0, 13.0, 14.0]
assert v1.size == 5
v1 = Vector([0.0, 1.0, 2.0, 3.0]) # with a list of floats
assert v1.values == [0.0, 1.0, 2.0, 3.0]
assert v1.size == 4

# add
v2 = v1 + 5
assert v1.values == [0.0, 1.0, 2.0, 3.0]
assert v2.values == [5.0, 6.0, 7.0, 8.0]
v2 = 5 + v1
assert v2.values == [5.0, 6.0, 7.0, 8.0]
v2 = v1 + v2
assert v2.values == [5.0, 7.0, 9.0, 11.0]

# sub
v2 = v1 - 5
assert v2.values == [-5.0, -4.0, -3.0, -2.0]
v2 = 5 - v1
assert v2.values == [-5.0, -4.0, -3.0, -2.0]
v2 = v1 - v2
assert v2.values == [5.0, 5.0, 5.0, 5.0]

# mul
v2 = v1 * 5
assert v2.values == [0.0, 5.0, 10.0, 15.0]
v2 = 5 * v1
assert v2.values == [0.0, 5.0, 10.0, 15.0]
dot_prod = v1 * v2
assert dot_prod == 70

# div
v2 = v1 / 5
assert v2.values == [0.0/5, 1.0/5, 2.0/5, 3.0/5]
v2 = 5 / v1
assert v2.values == [0.0/5, 1.0/5, 2.0/5, 3.0/5]

print('All good.')
