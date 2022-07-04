n = int(input())

students = tuple([input() for i in range(n)])

print(*students, sep='\n')
print()
for stud in students:
    if stud.split()[1] in '45':
        print(stud)