from functools import reduce

n = int(input())
words = [input() for i in range(n)]
words.sort()
words = sorted(words, key=lambda x: reduce(lambda a, b: a + (ord(b.upper()) - ord('A')), x, 0))
print(*words, sep='\n')