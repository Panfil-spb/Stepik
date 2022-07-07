file = open('nums.txt')

a, b = file.read().split()

print(int(a) + int(b))

file.close()