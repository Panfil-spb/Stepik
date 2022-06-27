list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
maximum = -1

for i in list1:
    maximum = max(i) if max(i) > maximum else maximum
print(maximum)




