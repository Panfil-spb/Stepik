# put your python code here
n = int(input())

res = []
for i in range(n):
    res.append(len(set(input().lower())))

for i in res:
    print(i)