n = int(input())
studs = set(input() for i in range(int(input())))
for i in range(1, n):
    studs &= set(input() for i in range(int(input())))
studs = sorted(list(studs))
print(*studs, sep='\n')