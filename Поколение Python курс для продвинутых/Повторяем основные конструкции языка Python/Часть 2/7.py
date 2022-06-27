s1 = input()
s2 = input()

if s1 == s2:
    print("ничья")
else:
    if s1 == 'камень' and s2 == 'бумага':
        print("Руслан")
    elif s1 == 'камень' and s2 == 'ножницы':
        print("Тимур")
    elif s1 == 'камень' and s2 == 'Спок':
        print("Руслан")
    elif s1 == 'камень' and s2 == 'ящерица':
        print("Тимур")

    elif s1 == 'бумага' and s2 == 'камень':
        print("Тимур")
    elif s1 == 'бумага' and s2 == 'ножницы':
        print("Руслан")
    elif s1 == 'бумага' and s2 == 'Спок':
        print("Тимур")
    elif s1 == 'бумага' and s2 == 'ящерица':
        print("Руслан")

    elif s1 == 'ножницы' and s2 == 'бумага':
        print("Тимур")
    elif s1 == 'ножницы' and s2 == 'камень':
        print("Руслан")
    elif s1 == 'ножницы' and s2 == 'Спок':
        print("Руслан")
    elif s1 == 'ножницы' and s2 == 'ящерица':
        print("Тимур")

    elif s1 == 'ящерица' and s2 == 'бумага':
        print("Тимур")
    elif s1 == 'ящерица' and s2 == 'камень':
        print("Руслан")
    elif s1 == 'ящерица' and s2 == 'Спок':
        print("Тимур")
    elif s1 == 'ящерица' and s2 == 'ножницы':
        print("Руслан")

    elif s1 == 'Спок' and s2 == 'бумага':
        print("Руслан")
    elif s1 == 'Спок' and s2 == 'камень':
        print("Тимур")
    elif s1 == 'Спок' and s2 == 'ящерица':
        print("Руслан")
    elif s1 == 'Спок' and s2 == 'ножницы':
        print("Тимур")

