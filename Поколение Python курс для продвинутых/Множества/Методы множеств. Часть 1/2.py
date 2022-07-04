# put your python code here
n = int(input())

s = ''

for i in range(n):
    s += input()

print(len(set(s.lower())))