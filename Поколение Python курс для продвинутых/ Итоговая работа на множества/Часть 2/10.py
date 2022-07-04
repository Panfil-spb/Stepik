m, n = int(input()), int(input())

set1 = set()

for i in range(n * m):
    name = input()
    if name in set1:
        set1.remove(name)
    else:
        set1.add(name)

if len(set1) == 0:
    print('NO')
else:
    print(len(set1))