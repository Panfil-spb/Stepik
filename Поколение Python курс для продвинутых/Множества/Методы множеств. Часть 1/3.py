# put your python code here
s = input().lower()

for i in '.,;:-?!':
    s = s.replace(i, '')

print(len(set(s.split())))