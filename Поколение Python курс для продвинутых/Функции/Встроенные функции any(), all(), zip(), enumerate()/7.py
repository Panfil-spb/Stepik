n = int(input())
otl = []
for i in range(n):
    k = int(input())
    res = []
    for j in range(k):
        student, mark = input().split()
        res.append(int(mark) == 5)
    otl.append(any(res))

if all(otl):
    print('YES')
else:
    print('NO')