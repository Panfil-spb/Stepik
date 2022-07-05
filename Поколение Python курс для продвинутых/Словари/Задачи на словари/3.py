s1 = input().lower()
s2 = input().lower()

for i in '.,!?:;- ':
    s1 = s1.replace(i, '')
    s2 = s2.replace(i, '')

res = {}

for i in s1:
    res[i] = res.get(i, 0) + 1

for i in s2:
    res[i] = res.get(i, 0) - 1

if set(res.values()) == {0}:
    print('YES')
else:
    print('NO')