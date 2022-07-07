file_name = input()

lines = []
with open(file_name, 'r', encoding='utf-8') as file:
    for line in file:
        lines.append(line.strip())
        if len(lines) > 10:
            lines.pop(0)
    print(*lines, sep='\n')