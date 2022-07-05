d = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}

s = input()

print(''.join(d[i] for i in s))