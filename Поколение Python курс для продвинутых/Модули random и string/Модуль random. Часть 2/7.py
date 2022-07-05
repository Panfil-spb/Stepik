import random

names = []
for i in range(int(input())):
    names.append(input())

secret_friends = names.copy()
while True:
    random.shuffle(secret_friends)
    flag = 1
    for i in range(len(secret_friends)):
        if names[i] == secret_friends[i]:
            flag = 0
    if flag:
        break

for i in zip(names, secret_friends):
    print(i[0] + ' - ' + i[1])