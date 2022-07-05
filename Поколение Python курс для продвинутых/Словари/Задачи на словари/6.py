res = {}

for i in range(int(input())):
    num, name = input().lower().split()
    res.setdefault(name, []).append(num)

mas = []
for i in range(int(input())):
    name = input().lower()
    if name not in res:
        mas.append('абонент не найден')
    else:
        mas.append(' '.join(i for i in res[name]))

print(*mas, sep='\n')