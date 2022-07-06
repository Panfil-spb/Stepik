s = input().split()
s.sort(key=lambda x: x.lower())
print(*s)