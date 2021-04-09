from random import randrange

def new_game():
    n = randrange(100)

    print('{Приветственное сообщение от игры}')
    count = 0
    while count < 5:
        count += 1
        input_num = int(input('Введите число: '))
        if input_num < n:
            print('Загаданное число больше')
            continue
        elif input_num > n:
            print('Загаданное число меньше')
            continue
        elif input_num == n:
            print('Поздравляю! Вы угадали')
            break
        elif count == 4:
            print(f'Вы проиграли. Было загадано: {n}')


new_game()
while True:
    _continue = input('Хотите начать сначала? (1 - ДА )')

    if _continue == '1':
        new_game()
    else:
        break
