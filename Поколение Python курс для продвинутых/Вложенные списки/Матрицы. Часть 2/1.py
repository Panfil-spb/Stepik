n, m = int(input()), int(input())

mat = []

for i in range(n):
    mat.append([])
    for j in range(m):
        mat[i].append(i * j)

for i in range(n):
    for j in range(m):
        print(str(mat[i][j]).ljust(3), end=' ')
    print()


