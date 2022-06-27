s = input().split()

res = []

for i in range(len(s)):
    if len(res) == 0:
        res.append([s[i]])
    else:
        if s[i] not in res[-1]:
            res.append([s[i]])
        else:
            res[-1].append(s[i])

print(res)
