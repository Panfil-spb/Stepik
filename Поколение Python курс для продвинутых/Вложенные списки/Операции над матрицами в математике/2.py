n, m = map(int, input().split())

mat1 = [[j for j in map(int, input().split())] for i in range(n)]

input()

m, k = map(int, input().split())

mat2 = [[j for j in map(int, input().split())] for i in range(m)]

res = [[0 for j in range(k)] for i in range(n)]

for i in range(n):
    for j in range(k):
        sum = 0
        for l in range(m):
            sum += mat1[i][l] * mat2[l][j]
        res[i][j] = sum

for i in range(n):
    for j in range(k):
        print(res[i][j], end=' ')
    print()