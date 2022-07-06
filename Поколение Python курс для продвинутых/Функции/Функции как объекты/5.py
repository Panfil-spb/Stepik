import math
n = int(input())
name = input()

d = {'квадрат': n ** 2,
     'куб': n ** 3,
     'корень': n ** 0.5,
     'модуль': abs(n),
     'синус':math.sin(n)}

print(d[name])