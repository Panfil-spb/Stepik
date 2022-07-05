import random

nums = set()

while len(nums) < 7:
    nums.add(random.randint(1, 49))

nums = sorted(nums)

print(*nums, sep=' ')