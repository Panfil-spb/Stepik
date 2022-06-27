n = int(input())

mat = []
counts = []
for i in range(n):
    mat.append([i for i in map(int, input().split())])
    s = sum(mat[i]) / n
    count = 0
    for j in mat[i]:
        if j > s:
            count += 1
    counts.append(count)

for i in counts:
    print(i)
