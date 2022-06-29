n, m = map(int, input().split())

mat = []
c = 1
for i in range(n):
    mat.append([])
    for j in range(m):
        if i % 2:
            mat[i].insert(0, c)
            mat[i].append(c)
        else:
            mat[i].append(c)

        c += 1

for i in range(n):
    for j in range(m):
        print(str(mat[i][j]).ljust(3), end=' ')
    print()
