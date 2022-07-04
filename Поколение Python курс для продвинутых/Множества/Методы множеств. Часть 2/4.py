# put your python code here
n = int(input())

s = set(input())
for i in range(1, n):
    s &= set(input())
s = [int(i) for i in s]
s.sort()
print(*s, sep=' ')