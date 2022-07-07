from random import choice

with open('first_names.txt') as names_file, open('last_names.txt') as second_names_file:

    names = list(map(str.strip, names_file.readlines()))
    second_names = list(map(str.strip, second_names_file.readlines()))
    names = [choice(names) for i in range(3)]
    second_names = [choice(second_names) for i in range(3)]
    answer = list(map(lambda x: f'{x[0]} {x[1]}', zip(names, second_names)))
    print(*answer, sep='\n')