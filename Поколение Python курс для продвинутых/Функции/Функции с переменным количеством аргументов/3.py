def mean(*args):
    new_mas = [i for i in args if type(i) is int or type(i) is float]
    if new_mas == []:
        return 0
    return sum(new_mas) / len(new_mas)

print(mean())
print(mean(7))
print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
print(mean(True, ['stepik'], 'beegeek', (1, 2)))
print(mean(-1, 2, 3, 10, ('5')))
print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))