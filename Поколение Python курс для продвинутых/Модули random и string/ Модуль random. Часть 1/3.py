import random

length = int(input())    # длина пароля

password = ''

for i in range(length):
    if i % 2:
        password += chr(random.randint(65, 90))
    else:
        password += chr(random.randint(97, 122))

print(password)