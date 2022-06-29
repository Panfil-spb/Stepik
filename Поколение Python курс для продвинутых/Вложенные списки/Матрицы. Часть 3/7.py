n, m = map(int, input().split())

mas = [i for i in range(1, m+1)]
for i in range(n):
    print(' '.join(str(k) for k in mas))
    mas = mas[1:] + [mas[0]]
    