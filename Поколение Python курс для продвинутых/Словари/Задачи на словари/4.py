n = int(input())

res = {}

for i in range(n):
    s = input().split()
    res[s[0]] = s[1]
    res[s[1]] = s[0]

print(res[input()])