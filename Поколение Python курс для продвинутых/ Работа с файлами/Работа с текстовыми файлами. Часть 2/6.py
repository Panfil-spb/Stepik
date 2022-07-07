from functools import reduce

with open('file.txt') as file:
    cout_line = 0
    count_word = 0
    count_letter = 0

    lines = file.readlines()
    cout_line = len(lines)
    count_word = reduce(lambda a, x: a + len(x.split()), lines, 0)
    count_letter = reduce(lambda a, x: a + reduce(lambda b, l: b + 1 if l.isalpha() else b + 0, x, 0), lines, 0)
    print(
        f"""Input file contains:
{count_letter} letters 
{count_word} words 
{cout_line} lines """)