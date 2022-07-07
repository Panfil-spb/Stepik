from functools import reduce

with open('numbers.txt') as file:
    lines = list(map(str.split, file.readlines()))
    lines = list(map(lambda line: reduce(lambda a, x: a + int(x), line, 0), lines))
    print(*lines, sep='\n')