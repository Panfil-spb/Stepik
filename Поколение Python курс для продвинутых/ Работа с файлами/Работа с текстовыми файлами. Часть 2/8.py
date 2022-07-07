from functools import reduce

with open('population.txt') as file:

    lines = list(map(lambda x: x.strip().split('\t'), file.readlines()))

    lines = list(filter(lambda x: x[0][0].upper() == 'G' and int(x[1]) > 500000, lines))

    lines = list(map(lambda x: x[0], lines))
    print(*lines, sep='\n')