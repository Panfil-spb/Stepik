s = input()

s_d = {}

for i in s:
    s_d[i] = s_d.get(i, 0) + 1

d = {}

for i in range(int(input())):
    st = input().split()
    for j in s_d:
        if s_d[j] == int(st[1]):
            s = s.replace(j, st[0][0])

print(s)
