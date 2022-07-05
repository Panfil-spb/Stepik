s = input()

d = {}

for i in s.split():
    d[i] = d.get(i, 0) + 1
    print(d[i], end=' ')