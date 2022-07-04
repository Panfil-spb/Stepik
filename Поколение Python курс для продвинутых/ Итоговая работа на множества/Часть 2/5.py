set1 = set(int(i) for i in input().split())
set2 = set(int(i) for i in input().split())

set3 = sorted(list(set1 & set2), reverse=True)

if len(set3) == 0:
    print('BAD DAY')
else:
    print(*list(set3), sep=' ')