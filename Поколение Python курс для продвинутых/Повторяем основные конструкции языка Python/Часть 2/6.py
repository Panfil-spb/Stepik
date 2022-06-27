n = int(input())

nums = [int(input()) for i in range(n)]

num = int(input())
ans = "НЕТ"
for i in range(n):
    for j in range(i+1, n):
        if nums[i] * nums[j] == num:
            s = "ДА"
print(s)
