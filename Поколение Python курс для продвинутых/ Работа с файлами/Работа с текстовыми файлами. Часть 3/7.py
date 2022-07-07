def func(line):
    start = line[1].split(':')
    start = int(start[0]) * 60 + int(start[1])
    stop = line[2].split(':')
    stop = int(stop[0]) * 60 + int(stop[1])
    if start > stop:
        stop += 24 * 60
    return stop - start >= 60

lines = []

with open('logfile.txt', encoding='utf-8') as file:
    lines = [line.strip().split(',') for line in file]

    lines = list(map(lambda x: x[0], filter(func, lines)))
    with open('output.txt', 'w', encoding='utf-8') as output_file:
        print(*lines, sep='\n', file=output_file)