with open('grades.txt', 'r', encoding='utf-8') as file:
    lines = list(map(str.strip, file.readlines()))
    lines = list(map(lambda line: line.split()[1:], lines))
    lines = list(filter(lambda line: int(line[0]) >= 65 and int(line[1]) >= 65 and int(line[2]) >= 65, lines))
    print(len(lines))