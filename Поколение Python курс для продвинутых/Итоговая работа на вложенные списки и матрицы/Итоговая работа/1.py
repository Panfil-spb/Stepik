s = input().split()
n = int(input())

res = [[] for i in range(n)]

for i in range(len(s)):
    res[i % n].append(s[i])

print(res)
