import string
import random


def generate_password(length):
    s = string.ascii_letters + string.digits
    no_s = 'lI1oO0'
    while True:
        flag1 = 0
        flag2 = 0
        flag3 = 0
        password = ''

        while len(password) != length:
            sim = random.choice(s)
            if sim not in no_s:
                password += sim
                if sim in string.digits:
                    flag1 = 1
                if sim in string.ascii_uppercase:
                    flag2 = 1
                if sim in string.ascii_lowercase:
                    flag3 = 1

        if flag1 and flag2 and flag3:
            return password


def generate_passwords(count, length):
    passwords = []
    for i in range(count):
        passwords.append(generate_password(length))
    return passwords


n, m = int(input()), int(input())

pas = generate_passwords(n, m)

print(*pas, sep='\n')