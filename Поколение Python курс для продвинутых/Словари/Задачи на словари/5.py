n = int(input())

res = {}

for i in range(n):
    s = input().split()
    for i in s[1:]:
        res[i] = s[0]

mas = []

for i in range(int(input())):
    mas.append(res[input()])

print(*mas, sep='\n')