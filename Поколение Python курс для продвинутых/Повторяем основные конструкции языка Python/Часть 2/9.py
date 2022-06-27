s = [input() for i in range(int(input()))]
p = 'anton'
for i in range(len(s)):
    for j in s[i]:
        if j not in p:
            s[i] = s[i].replace(j, '')
    c = 0
    for j in s[i]:
        if c < 5 and p[c] == j:
            c += 1
    if c == 5:
        print(i + 1, end=' ')