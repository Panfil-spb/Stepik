def func(index):
    def g(mas):
        return mas[index - 1]
    return g

athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
i = int(input())
athletes.sort(key=func(i))
for i in athletes:
    print(*i, sep=' ')
