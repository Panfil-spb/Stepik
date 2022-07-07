
with open('goats.txt', encoding='utf-8') as file, open('answer.txt', 'w') as answer:
    file.readline()
    lines = file.read().split('GOATS')
    colors = {x: 0 for x in lines[0].strip().split('\n')}

    goats = lines[1].strip().split('\n')

    counts = len(goats)

    for goat in goats:
        colors[goat] += 1
    colors = list(filter(lambda x: colors[x] * 100 > 7 * counts, colors))
    colors.sort()
    print(*colors, sep='\n', file=answer)