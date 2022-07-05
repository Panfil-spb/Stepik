s1 = input()
s2 = input()

res = {}
s = 'YES'
for i in s1:
    res[i] = res.get(i, 0) + 1

for i in s2:
    if i not in res:
        s = 'NO'
        break
    else:
        res[i] = res[i] - 1

for i in res:
    if res[i] != 0:
        s = 'NO'
        break

print(s)