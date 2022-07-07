from functools import reduce

d = {
    'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v', 'м': 'm', 'ч': 'ch',
    'г': 'g', 'н': 'n', 'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*',
    'ё': 'jo', 'р': 'r', 'ы': 'y', 'ж': 'zh', 'с': 's', 'ь': "'", 'з': 'z', 'т': 't', 'э': 'je',
    'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j', 'ф': 'f', 'я': 'ya'
    }

with open('cyrillic.txt', 'r', encoding='utf-8') as read_file:
    text = read_file.read()
    text = reduce(lambda a, x: a + x if x.lower()
                                        not in d else a + d[x.lower()].capitalize() if x.isupper()
    else a + d[x.lower()], text, '')

    with open('transliteration.txt', 'w', encoding='utf-8') as write_file:
        print(text, file=write_file)