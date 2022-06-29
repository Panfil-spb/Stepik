n, m = map(int, input().split())
mt = [[0 for j in range(m)] for i in range(n)]
c = 1
i, j = 0, 0

while c <= n * m:
    while j < m and mt[i][j] == 0:
        mt[i][j] = c
        c += 1
        j += 1
    j -= 1
    i += 1
    while i < n and mt[i][j] == 0:
        mt[i][j] = c
        c += 1
        i += 1
    i -= 1
    j -= 1
    while j >= 0 and mt[i][j] == 0:
        mt[i][j] = c
        c += 1
        j -= 1
    j += 1
    i -= 1
    while i >= 0 and mt[i][j] == 0:
        mt[i][j] = c
        c += 1
        i -= 1
    i += 1
    j += 1

[print(*r, sep=' ') for r in mt]