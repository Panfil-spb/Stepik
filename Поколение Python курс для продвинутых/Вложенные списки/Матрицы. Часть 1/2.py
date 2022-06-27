n, m = int(input()), int(input())

matr = []
for i in range(n):
    matr.append([])
    for j in range(m):
        matr[i].append(input())

for i in matr:
    print(' '.join(j for j in i))

print()

for i in range(m):
    for j in range(n):
        print(matr[j][i], end=' ')
    print()
