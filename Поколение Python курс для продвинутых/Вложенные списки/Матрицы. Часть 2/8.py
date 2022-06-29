# put your python code here
s = input()

n, m = ord(s[0]) - ord('a'), 8 - int(s[1])

mat = [['.' for j in range(8)] for i in range(8)]

mat[m][n] = 'N'

if m + 2 < 8 and n + 1 < 8:
    mat[m + 2][n + 1] = '*'
if m + 2 < 8 and n - 1 >= 0:
    mat[m + 2][n - 1] = '*'

if m - 2 >= 0 and n + 1 < 8:
    mat[m - 2][n + 1] = '*'
if m - 2 >= 0 and n - 1 >= 0:
    mat[m - 2][n - 1] = '*'

if m + 1 < 8 and n + 2 < 8:
    mat[m + 1][n + 2] = '*'
if m - 1 >= 0 and n + 2 < 8:
    mat[m - 1][n + 2] = '*'

if m + 1 < 8 and n - 2 >= 0:
    mat[m + 1][n - 2] = '*'
if m - 1 >= 0 and n - 2 >= 0:
    mat[m - 1][n - 2] = '*'

for i in range(8):
    for j in range(8):
        print(mat[i][j], end=' ')
    print()