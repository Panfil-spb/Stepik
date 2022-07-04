words = set()

for i in range(int(input())):
    words.add(input())

if input() in words:
    print('REPEAT')
else:
    print('OK')