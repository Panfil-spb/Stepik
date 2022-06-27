n = int(input())
mat = []
for i in range(n):
    mat.append([j for j in map(int, input().split())])
sum = [0 for i in range(4)]
m = mat[0][0]
for i in range(n):
    for j in range(n):
        if i < j and i < n - 1- j:
            sum[0] += mat[i][j]
        elif i < j and i > n - 1 - j:
            sum[1] += mat[i][j]
        elif i > j and i > n - 1 - j:
            sum[2] += mat[i][j]
        elif i > j and i < n - 1 - j:
            sum[3] += mat[i][j]

print("Верхняя четверть: " + str(sum[0]))
print("Правая четверть: " + str(sum[1]))
print("Нижняя четверть: " + str(sum[2]))
print("Левая четверть: " + str(sum[3]))