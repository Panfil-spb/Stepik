n = int(input())

res = {}

for i in range(n):
    s = input().split(':')
    res[s[0].lower()] = s[1].strip()

n = int(input())
mas = []

for i in range(n):
    mas.append(input().lower())

for i in mas:
    print(res.get(i, 'Не найдено'))