with open('ledger.txt', 'r', encoding='utf-8') as file:
    lines = list(map(lambda line: int(line[1:]),file.readlines()))
    print('$' + str(sum(lines)))