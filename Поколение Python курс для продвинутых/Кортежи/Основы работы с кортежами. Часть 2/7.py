n = int(input())
tr = (1, 1, 1)

for i in range(3, n):
    tr += (sum(tr[i-3:i]), )

for i in range(n):
    print(tr[i], end=' ')