n = int(input())

for i in range(n):
    for j in range(n):
        num = 0
        if i == j:
            num = 1
        elif n - j - 1 == i:
            num = 1
        print(num, end=' ')
    print()