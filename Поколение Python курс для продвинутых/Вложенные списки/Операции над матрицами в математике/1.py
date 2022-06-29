n, m = map(int, input().split())

mat1 = [[j for j in map(int, input().split())] for i in range(n)]

input()

mat2 = [[j for j in map(int, input().split())] for i in range(n)]

for i in range(n):
    for j in range(m):
        print(mat1[i][j] + mat2[i][j], end=' ')
    print()