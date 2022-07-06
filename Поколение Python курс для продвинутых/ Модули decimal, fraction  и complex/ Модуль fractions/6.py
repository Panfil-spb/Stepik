from fractions import Fraction as F
from math import factorial
n = int(input())

s = F(0)
for i in range(1, n + 1):
     s += F(1, factorial(i))
print(s)