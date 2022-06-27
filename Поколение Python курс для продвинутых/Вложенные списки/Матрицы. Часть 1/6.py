n = int(input())
mat = []
for i in range(n):
    mat.append([j for j in map(int, input().split())])

m = mat[0][0]
for i in range(n):
    for j in range(n):
        if (i >= j and i <= n - 1 - j) or (i <= j and i >= n - 1 - j):

            m = max(m, mat[i][j])

print(m)
