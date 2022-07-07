with open('text.txt') as file:
    line = file.read().strip()
    print(*line[::-1], sep='')