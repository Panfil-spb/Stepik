s = input().split()
res = {}

for i, el in enumerate(s):
    if el in res:
        s[i] += f'_{res[el]}'
        res[el] += 1
    else:
        res[el] = 1

print(*s, sep=' ')
