n = int(input())

mat = [[j for j in map(int, input().split())] for i in range(n)]
maximum = mat[0][-1]
for i in range(n):
    for j in range(n):
        if (i <= j and i >= n - j - 1) or (i >= j and i >= n - j - 1):
            maximum = max(maximum, mat[i][j])
print(maximum)
