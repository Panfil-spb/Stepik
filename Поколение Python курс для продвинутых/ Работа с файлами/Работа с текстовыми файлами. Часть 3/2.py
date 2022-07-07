import random
with open('random.txt', 'w') as file:
    nums = list(map(lambda x: str(random.randint(111, 777)) + '\n', range(25)))
    file.writelines(nums)