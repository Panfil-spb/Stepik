# put your python code here
s1, s2, s3 = set(input().split()), set(input().split()), set(input().split())

s = [int(i) for i in s3 - s2 - s1]

s.sort(reverse=True)

for i in s:
    print(i, end=' ')