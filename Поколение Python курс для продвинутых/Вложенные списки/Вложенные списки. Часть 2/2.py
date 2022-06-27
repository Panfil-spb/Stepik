n = int(input())

res = [[j+1 for j in range(i+1)] for i in range(n)]
for i in res:
    print(i)