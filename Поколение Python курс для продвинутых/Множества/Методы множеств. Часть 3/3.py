# put your python code here
s1, s2, s3 = set(input().split()), set(input().split()), set(input().split())

s = [int(i) for i in s1 & s2 - s3]

s.sort()

for i in s[::-1]:
    print(i, end=' ')