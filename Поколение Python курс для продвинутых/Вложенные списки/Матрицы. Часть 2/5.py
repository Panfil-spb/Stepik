n = int(input())

mat = []

for i in range(n):
    mat.append([int(j) for j in input().split()])

for i in range(n // 2):
    mat[i][i], mat[n - i - 1][i] = mat[n - i - 1][i], mat[i][i]
    mat[i][n-i-1], mat[n-i-1][n-i-1] = mat[n-i-1][n-i-1], mat[i][n-i-1]

for i in range(n):
    for j in range(n):
        print(mat[i][j], end=' ')
    print()