
with open('input.txt') as input_file, open('output.txt', 'w') as output_file:
    lines = input_file.readlines()
    lines = list(map(lambda x: f'{x[0]}) {x[1]}', zip(range(1, len(lines) + 1), lines)))
    output_file.writelines(lines)
