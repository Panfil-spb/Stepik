import random
import string
def generate_index():
    index = ''
    index += random.choice(string.ascii_uppercase)
    index += random.choice(string.ascii_uppercase)
    index += str(random.randint(0, 99))
    index += '_'
    index += str(random.randint(0, 99))
    index += random.choice(string.ascii_uppercase)
    index += random.choice(string.ascii_uppercase)
    return index
