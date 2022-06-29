n, m = map(int, input().split())

for i in range(n):
    for j in range(m):
        print(n * j + i + 1, end=' ')
    print()