from fractions import Fraction as F
from math import gcd
n = int(input())

a, b = 1, n - 1

maximum = F(a, b)

for i in range(n):
    a += 1
    b -= 1
    if gcd(a, b) == 1 and a < b:
        maximum = max(maximum, F(a, b))

print(maximum)