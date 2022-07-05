import random

n = int(input())    # количество попыток

for i in range(n):
    if random.randrange(2):
        print('Орел')
    else:
        print('Решка')