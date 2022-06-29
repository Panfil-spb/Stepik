# put your python code here
n = int(input())

mat = []

for i in range(n):
    mat.append([i for i in map(int, input().split())])
s = sum(mat[0])
st = 'YES'

for i in range(n):
    if sum(mat[i]) != s:
        st = 'NO'
        break
    if sum([mat[j][i] for j in range(n)]) != s:
        st = 'NO'

        break
if sum([mat[i][i] for i in range(n)]) != s:
    st = 'NO'

if sum([mat[i][n - i - 1] for i in range(n)]) != s:
    st = 'NO'

k = []

for i in range(n):
    for j in range(n):
        if mat[i][j] not in k and mat[i][j] != 0 and mat[i][j] <= n * n:
            k.append(mat[i][j])
        else:
            st = 'NO'
            break
print(st)