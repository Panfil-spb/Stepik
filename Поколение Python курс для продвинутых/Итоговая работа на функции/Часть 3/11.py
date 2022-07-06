from functools import reduce

n = int(input())
ips = [input() for i in range(n)]

ips = sorted(ips, key=lambda x: reduce(lambda a, b: a * 256 + b, list(map(int, x.split('.'))), 0))

print(*ips, sep='\n')