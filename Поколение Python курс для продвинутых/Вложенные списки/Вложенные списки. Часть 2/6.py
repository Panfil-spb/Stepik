s = input().split()

res = [[]]
for i in range(1, len(s)+1):
    for j in range(0, len(s)):
        if j + i <= len(s):
            res.append(s[j:j+i])
print(res)