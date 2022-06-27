n = int(input())
mat = []
for i in range(n):
    mat.append([j for j in map(int, input().split())])

m = mat[0][0]
for i in range(n):
    for j in range(n):
        if j <= i:
            m = max(m, mat[i][j])

print(m)
