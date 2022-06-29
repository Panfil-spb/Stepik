n, m = int(input()), int(input())

mat = []

for i in range(n):
    mat.append([int(j) for j in input().split()])

ij= input().split()
ij[0] = int(ij[0])
ij[1] = int(ij[1])

for k in range(n):
    mat[k][ij[0]], mat[k][ij[1]] = mat[k][ij[1]], mat[k][ij[0]]

for i in range(n):
    for j in range(m):
        print(mat[i][j], end=' ')
    print()