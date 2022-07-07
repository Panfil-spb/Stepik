file = open('numbers.txt')

a, b = file

print(sum(int(a), int(b)))

file.close()