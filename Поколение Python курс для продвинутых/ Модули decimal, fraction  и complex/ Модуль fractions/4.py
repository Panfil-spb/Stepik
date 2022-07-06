from fractions import Fraction as F
s1 = input()
s2 = input()
a = F(s1)
b = F(s2)

print(f"{s1} + {s2} = {a + b}")
print(f"{s1} - {s2} = {a - b}")
print(f"{s1} * {s2} = {a * b}")
print(f"{s1} / {s2} = {a / b}")