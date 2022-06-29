# put your python code here
n = int(input())

for i in range(n):
    for j in range(n):
        if i == n - 1 - j:
            print(1, end=' ')
        elif i < n - j - 1:
            print(0, end=' ')
        else:
            print(2, end=' ')
    print()