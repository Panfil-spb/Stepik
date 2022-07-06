from fractions import Fraction as F
from math import gcd

n = int(input())

nums = []

for i in range(1, n + 1):
    for j in range(1, n):
        num = F(j, i)
        if num < 1 and gcd(i, j) == 1:
            nums.append(num)

nums.sort()

print(*nums, sep='\n')