import string

password = input()

if all([any(i in password for i in string.ascii_lowercase),
          any(i in password for i in string.ascii_uppercase),
          any(i in password for i in string.digits),
          len(password) >= 7]):
    print('YES')
else:
    print('NO')