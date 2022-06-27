m = float(input())
h = float(input())

indx = m / h ** 2

if 18.5 <= indx <= 25:
    print("Оптимальная масса")
elif indx < 18.5:
    print("Недостаточная масса")
else:
    print("Избыточная масса")