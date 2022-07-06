a, b = int(input()), int(input())
mas = list(range(1, b + 1))
mas = list(filter(lambda x: '0' not in str(x) and all(x % int(i) == 0 for i in str(x)), mas))
print(*mas)