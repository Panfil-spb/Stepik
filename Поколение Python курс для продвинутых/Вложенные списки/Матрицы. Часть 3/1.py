# put your python code here
k = input().split()

n, m = int(k[0]), int(k[1])

mat = []
for i in range(n):
    for j in range(m):
        if (i + j) % 2 == 0:

            print('.', end=' ')
        else:
            print('*', end=' ')

    print()