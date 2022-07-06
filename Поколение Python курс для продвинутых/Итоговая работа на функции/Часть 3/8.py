def arithmetic_operation(sign):
    if sign == '+':
        return lambda a, b: a + b
    elif sign == '-':
        return lambda a, b: a - b
    elif sign == '*':
        return lambda a, b: a * b
    elif sign == '/':
        return lambda a, b: a / b


add = arithmetic_operation('+')
div = arithmetic_operation('/')
print(add(10, 20))
print(div(20, 5))
