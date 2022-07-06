def my_sort(num):
    return sum([int(i) for i in num])

nums = input().split()
nums.sort(key=int)
nums.sort(key=my_sort)

print(*nums)