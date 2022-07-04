# put your python code here
s = input()

n, m = ord(s[0]) - ord('a'), 8 - int(s[1])

mat = [['.' for j in range(8)] for i in range(8)]

for i in range(8):
    mat[i][n] = '*'
    mat[m][i] = '*'

for i in range(8):
    for j in range(8):
        if i - j == m - n:
            mat[i][j] = '*'

        if i + j == m + n:
            mat[i][j] = '*'


mat[m][n] = 'Q'


for i in range(8):
    for j in range(8):
        print(mat[i][j], end=' ')
    print()
