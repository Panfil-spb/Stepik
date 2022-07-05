d = {}
dd = {'read': 'R',
      'write': 'W',
      'execute': 'X'}

for i in range(int(input())):
    name, *actions = input().split()
    d[name] = actions

for i in range(int(input())):
    action, name = input().split()
    if dd[action] in d[name]:
        print('OK')
    else:
        print('Access denied')
