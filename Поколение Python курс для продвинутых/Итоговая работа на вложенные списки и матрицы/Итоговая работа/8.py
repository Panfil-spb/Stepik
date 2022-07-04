n = int(input())

mat = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    c = 0
    for j in range(i, n):
        mat[i][j] = c
        mat[j][i] = c
        c += 1

for i in range(n):
    for j in range(n):
        print(mat[i][j], end=' ')
    print()
