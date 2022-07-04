# put your python code here
s = set(range(11))
for i in range(3):
    s -= set([int(i) for i in input().split()])

s = list(s)
s.sort()

print(*s, sep=' ')