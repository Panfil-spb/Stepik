import string
import random

def generate_password(length):
    s = string.ascii_letters + string.digits
    no_s = 'lI1oO0'
    password = ''
    while len(password) != length:
        sim = random.choice(s)
        if sim not in no_s:
            password += sim
    return password

def generate_passwords(count, length):
    passwords = []
    for i in range(count):
        passwords.append(generate_password(length))
    return passwords
n, m = int(input()), int(input())

pas = generate_passwords(n, m)

print(*pas, sep='\n')
