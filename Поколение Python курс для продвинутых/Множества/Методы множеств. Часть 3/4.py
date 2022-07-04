# put your python code here

s1, s2, s3 = set(input().split()), set(input().split()), set(input().split())

s = (s1 & s2 - s3) | (s1 & s3 - s2) | (s2 & s3 - s1) | (s1 - s2 - s3) | (s2 - s3 - s1) | (s3 - s2 - s1)

s = [int(i) for i in s]

s.sort()

for i in s:
    print(i, end=' ')