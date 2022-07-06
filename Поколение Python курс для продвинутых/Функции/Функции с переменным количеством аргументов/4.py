def greet(name, *args):
    if len(args) == 0:
        return 'Hello, ' + name +'!'
    else:
        return 'Hello, ' + name + ' and ' + ' and '.join(name for name in args) + '!'


print(greet('Timur'))
print(greet('Timur', 'Roman'))
print(greet('Timur', 'Roman', 'Ruslan'))