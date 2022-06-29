n = int(input())

mat = []

for i in range(n):
    mat.append([int(j) for j in input().split()])

s = "YES"

for i in range(n):
    for j in range(i + 1):
        if mat[i][j] != mat[j][i]:
            s = "NO"

print(s)
