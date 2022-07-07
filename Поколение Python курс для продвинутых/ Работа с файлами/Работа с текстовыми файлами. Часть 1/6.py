from functools import reduce

file = open('prices.txt')

data = reduce(lambda a, x: a + int(x.split()[1]) * int(x.split()[2]), file.readlines(), 0)

print(data)

file.close()