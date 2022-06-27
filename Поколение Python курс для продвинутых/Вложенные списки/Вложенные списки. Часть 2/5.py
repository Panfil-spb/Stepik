s = input().split()
n = int(input())

res = []
for i in range(0, len(s), n):
    res.append(s[i:i+n])

print(res)
