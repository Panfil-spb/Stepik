b = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и',
     'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с',
     'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ',
     'ы', 'ь', 'э', 'ю', 'я']

s = input() + " запретил букву"
for i in b:
     if i in s:
          print(s + ' ' + i)
          s = s.replace(i, '').strip()
          s = s.replace('  ', ' ')