# put your python code here
s = input().split()

res = set()

for i in s:
    if int(i) not in res:
        print("NO")
        res.add(int(i))
    else:
        print("YES")