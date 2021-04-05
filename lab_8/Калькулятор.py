
def calc():
    expression = input("Введите выражение: ").split()

    if expression[1] == '+':
        print(int(expression[0], 10) + int(expression[2], 10))
    elif expression[1] == '-':
        print(int(expression[0], 10) - int(expression[2], 10))
    elif expression[1] == '*':
        print(int(expression[0], 10) * int(expression[2], 10))
    elif expression[1] == '/':
        print(int(expression[0], 10) / int(expression[2], 10))
    else:
        print('Неправильно введенное выражение')

    exit()


calc()
