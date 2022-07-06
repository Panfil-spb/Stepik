def print_products(*args):
    count = 0
    for i in args:
        if type(i) is str and len(i) != 0:
            count += 1
            print(str(count) + ') ' + i)
    if count == 0:
        print('Нет продуктов')

print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)