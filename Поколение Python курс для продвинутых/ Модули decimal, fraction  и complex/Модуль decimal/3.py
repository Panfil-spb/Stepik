from decimal import *
num = Decimal(input())
sign, nums, count = num.as_tuple()
if -1 < num < 1:
    print(0 + max(nums))
else:
    print(min(nums) + max(nums))