n = input()
len = len(n)
for i in range(len):
    if (len - i - 1) % 3 == 0 and len - i - 1 != 0:
        print(n[i], end='')
        print(',', end='')
    else:
        print(n[i], end='')