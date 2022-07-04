m, n = int(input()), int(input())

math = set(input() for i in range(m))
info = set(input() for i in range(n))
print(len(math - info))