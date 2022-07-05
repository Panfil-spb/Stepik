import random

s = [i for i in input()]
random.shuffle(s)
print(''.join(i for i in s))