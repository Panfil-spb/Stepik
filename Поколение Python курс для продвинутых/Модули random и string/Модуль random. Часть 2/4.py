import random

numbers = set()

while len(numbers) != 100:
    s = str(random.randint(1, 9))
    s += ''.join(str(random.randint(0, 9)) for i in range(6))
    if s not in numbers:
        print(s)
        numbers.add(s)