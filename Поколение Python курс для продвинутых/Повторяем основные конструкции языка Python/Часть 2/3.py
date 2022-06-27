nums = [i for i in map(int, input().split())]

for i in range(0, len(nums), 2):
    if i < len(nums):
        nums[i], nums[i+1] = nums[i+1], nums[i]

print(' '.join(i for i in nums))