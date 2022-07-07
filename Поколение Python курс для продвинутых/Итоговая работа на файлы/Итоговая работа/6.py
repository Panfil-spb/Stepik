from functools import reduce

forb_words = []

with open('forbidden_words.txt', 'r', encoding='utf-8') as file:
    forb_words = file.read().strip().split()

with open(input(), 'r+') as file:
    text = file.read()
    corr_text = text.lower()
    for word in forb_words:
        corr_text = corr_text.replace(word, '*'*len(word))
    text = reduce(lambda a, x: a + x[0] if x[1] != '*' else a + x[1], zip(text, corr_text), '')
    print(text)