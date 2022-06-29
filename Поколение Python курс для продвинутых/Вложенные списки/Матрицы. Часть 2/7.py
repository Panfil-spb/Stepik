# put your python code here
n = int(input())

mat = []
res = []
for i in range(n):
    mat.append([i for i in map(int, input().split())])
    res.append([])


for i in range(n):
    for j in range(n-1, -1, -1):
        print(mat[j][i], end=" ")
    print()
