nums =[i for i in map(int, input().split())]
count = 0
j = 0
for i in range(1, len(nums)):
    count = count + 1 if nums[i] > nums[j] else count
    j += 1
print(count)