n = int(input())

res = [[1], [1, 1]]
for i in range(2, n+1):
    res.append([])
    for j in range(i+1):
        if j == 0 or j == i:
            res[i].append(1)
        else:
            res[i].append(res[i-1][j-1] + res[i-1][j])
for i in range(n):
    print(' '.join(str(j) for j in res[i]))
