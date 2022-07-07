with open('lines.txt') as file:
    lines = list(map(str.strip, file.readlines()))
    max_len = len(max(lines, key=len))

    lines = list(filter(lambda x: len(x) == max_len, lines))
    print(*lines, sep='\n')