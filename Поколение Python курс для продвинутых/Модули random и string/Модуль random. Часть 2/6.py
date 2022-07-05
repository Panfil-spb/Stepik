import random
use_numbers = set()
mat = []
for i in range(5):
    mat.append([])
    for j in range(5):
        while True:
            num = random.randint(1, 75)
            if num not in use_numbers:
                use_numbers.add(num)
                mat[i].append(num)
                break

mat[2][2] = 0
for i in mat:
    for j in i:
        print(str(j).ljust(3), end=' ')
    print()