n = int(input())

mat = [[j for j in map(int, input().split())] for i in range(n)]

shab = [i for i in range(1, n+1)]

s = 'YES'

for i in range(n):
    copy = shab[:]
    for j in mat[i]:
        if j in copy:
            copy.remove(j)
    if len(copy) != 0:
        s = 'NO'
        break

    copy = shab[:]
    for j in range(n):
        if mat[j][i] in copy:
            copy.remove(mat[j][i])
    if len(copy) != 0:
        s = 'NO'
        break

print(s)
