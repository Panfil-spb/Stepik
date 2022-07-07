from functools import reduce

with open('nums.txt') as file:
    lines = list(map(lambda x: x if x.isdigit() else ' ', file.read()))
    lines = reduce(lambda a, x: a + x, lines, '').split()
    nums = list(map(int, lines))
    print(sum(nums))