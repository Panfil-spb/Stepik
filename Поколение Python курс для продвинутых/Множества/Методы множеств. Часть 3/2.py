# put your python code here
s1, s2 = set(input()), set(input())

if s1.issuperset(s2):
    print('YES')
else:
    print('NO')