scrabble = {
    'AEILNORSTU' : 1,
    'DG' : 2,
    'BCMP' : 3,
    'FHVWY' : 4,
    'K' : 5,
    'JX' : 8,
    'QZ' : 10}

s = input()

sum_letters = 0
for i in s.upper():
    for j in scrabble:
        if i in j:
            sum_letters += scrabble[j]
print(sum_letters)