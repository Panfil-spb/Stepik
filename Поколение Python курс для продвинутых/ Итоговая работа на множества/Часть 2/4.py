m, n = int(input()), int(input())
books = {input() for i in range(m)}
list_book = [input() for i in range(n)]
for book in list_book:
    if book in books:
        print('YES')
    else:
        print('NO')