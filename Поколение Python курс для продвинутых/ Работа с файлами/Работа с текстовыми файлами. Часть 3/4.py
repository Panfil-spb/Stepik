
lines = []
with open('class_scores.txt', encoding='utf-8') as file:
    lines = list(map(lambda x: x.strip().split(), file.readlines()))
    lines = list(map(lambda x: [x[0], '100' if int(x[1]) + 5 >= 100 else str(int(x[1]) + 5)], lines))

with open('new_scores.txt', 'w', encoding='utf-8') as file:
    lines = list(map(lambda x: f'{x[0]} {x[1]}', lines))
    print(*lines, sep='\n', file=file)
