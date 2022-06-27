nums = [i for i in map(int, input().split())]

nums.insert(0, nums.pop())

print(' '.join(str(i) for i in nums))