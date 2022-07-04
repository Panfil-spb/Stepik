n = int(input())

mat1 = [[j for j in map(int, input().split())] for i in range(n)]

s = int(input())

res = [[mat1[i][j] for j in range(n)] for i in range(n)]

for p in range(1, s):
    tmp = [[res[i][j] for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            sum = 0
            for l in range(n):
                sum += tmp[i][l] * mat1[l][j]
            res[i][j] = sum

for i in range(n):
    for j in range(n):
        print(res[i][j], end=' ')
    print()