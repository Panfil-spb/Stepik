# put your python code
s1 = set(input().split())
s2 = set(input().split())

s3 = s1 & s2

s3 = [int(i) for i in s3]
s3.sort()
for i in s3:
    print(int(i), end=' ')