n = int(input())

mat = []

for i in range(n):
    mat.append(input().split())

sum = 0
for i in range(n):
    sum += int(mat[i][i])
print(sum)