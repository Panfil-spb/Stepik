m, n = int(input()), int(input())

math = set(input() for i in range(m))
info = set(input() for i in range(n))
l = len(math ^ info)

if l == 0:
    print('NO')
else:
    print(l)