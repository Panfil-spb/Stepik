from functools import reduce

def pretty_print(data, side='-', delimiter='|'):
    l = len(data) - 1 + len(data) * 2

    for i in map(str, data):
        l += len(i)

    print(' ' + side * l)
    print(reduce(lambda s, x: s + str(x) + f' {delimiter} ', data, f'{delimiter} '))
    print(' ' + side * l)


pretty_print([1, 2, 10, 23, 123, 3000])
pretty_print(['abc', 'def', 'ghi', '12345'])
pretty_print(['abc', 'def', 'ghi'], side='*')
pretty_print(['abc', 'def', 'ghi'], delimiter='#')
pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')

