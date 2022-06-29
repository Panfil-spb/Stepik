n, m = int(input()), int(input())

mat = []

for i in range(n):
    mat.append([int(j) for j in input().split()])

ma = mat[0][0]
mj = mi = 0

for i in range(n):
    for j in range(0, m):
        if ma < mat[i][j]:
            ma = mat[i][j]
            mj, mi = j, i

print(mi, mj)