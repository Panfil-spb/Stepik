n = int(input())

mat = []

for i in range(n):
    mat.insert(0, [int(j) for j in input().split()])

for i in range(n):
    for j in range(n):
        print(mat[i][j], end=' ')
    print()