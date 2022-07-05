shops = {}

for i in range(int(input())):
    name, item, count = input().split()
    if name in shops:
        shops[name][item] = shops[name].get(item, 0) + int(count)
    else:
        shops[name] = {}
        shops[name][item] = shops[name].get(item, 0) + int(count)

for name in sorted(shops):
    print(name + ':')
    for item in sorted(shops[name]):
        print(item + ' ' + str(shops[name][item]))