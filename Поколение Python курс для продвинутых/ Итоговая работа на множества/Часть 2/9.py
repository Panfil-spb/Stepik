set1 = set(input().split())
set2 = set(input().split())
set3 = sorted(list(set1 | set2))

print(*set3, sep=' ')