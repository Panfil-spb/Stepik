from functools import reduce

coefficients = list(map(int, input().split()))
x = int(input())

evaluate = lambda coefficients, x: reduce(lambda s, a: s * x + a, coefficients, 0)
print(evaluate(coefficients, x))