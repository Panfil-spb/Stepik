with open('data.txt') as file:
    lines = file.readlines()
    lines.reverse()
    for i in lines:
        print(i, end='')