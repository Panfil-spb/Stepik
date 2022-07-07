with open('words.txt', 'r', encoding='utf-8') as file:
    lines = file.read().strip().split()
    max_lenth = len(max(lines, key=len))
    lines = list(filter(lambda x: len(x) == max_lenth, lines))
    print(*lines, sep='\n')