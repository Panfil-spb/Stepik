funcs = []

with open(input(), 'r', encoding='utf-8') as file:
    text = file.readlines()
    for i, line in enumerate(text):
        new_line = line.split()
        if len(new_line) != 0 and 'def' == new_line[0] and i == 0:
            funcs.append(line.split()[1].split('(')[0])
        elif len(new_line) != 0 and 'def' == new_line[0] and text[i - 1][0] != '#':
            funcs.append(line.split()[1].split('(')[0])

if len(funcs) != 0:
    print(*funcs, sep='\n')
else:
    print('Best Programming Team')