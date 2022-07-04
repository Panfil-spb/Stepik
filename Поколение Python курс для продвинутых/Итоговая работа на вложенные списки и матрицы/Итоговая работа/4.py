n = int(input())

res = [['.' for i in range(n)] for j in range(n)]

for i in range(n):
    res[n//2][i] = '*'
    res[i][n//2] = '*'
    res[i][i] = '*'
    res[i][n-i-1] = '*'

for i in range(n):
    for j in range(n):
        print(res[i][j], end=' ')
    print()