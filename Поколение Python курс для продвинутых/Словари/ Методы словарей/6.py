s = input()

for i in '.,!?:;-':
    s = s.replace(i, '')
s = s.lower().split()

res = {}
for i in s:
    res[i] = res.get(i, 0) + 1

res = list(res.items())
res.sort(key=lambda x: x[1])
min_count = res[0][1]
res = [i for i in res if i[1] == min_count]
res.sort()
print(res[0][0])