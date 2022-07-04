n = int(input())

mat = [[j for j in map(int, input().split())] for i in range(n)]
s = 'YES'
for i in range(n):
    for j in range(n-i-1):
        if mat[i][j] != mat[n-j-1][n-i-1]:
            s = 'NO'
print(s)