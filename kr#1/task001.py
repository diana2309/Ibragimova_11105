import functools
from functools import reduce

# 1(a)
fact = lambda x: 1 if x < 1 else x * fact(x-1)
print(fact(5))

# 1(b)
n = int(input())
fac = map(lambda n: reduce(lambda x, y: x * y, range(1, n +1)), range(1, n+1))

fac_rad = list(map(lambda x: x ** 0.5, fac))
print(fac_rad)
