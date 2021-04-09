def find_num_of_tickets():
    tickets_num = int(input('Введите количество билетов Сигизмунда в промежутке 1 <= x <= 10^9: '))
    tickets = input('Введите билеты через пробел: ').split(' ')

    if len(tickets) != tickets_num:
        print('Неправильное количество билетов')
        exit(-1)

    found = False

    for i in range(0, len(tickets)):
        tickets_item = list(tickets[i])
        code = [tickets_item[0], tickets_item[4], tickets_item[5], tickets_item[6], tickets_item[7], tickets_item[8]]
        if code == ["a", "5", "5", "6", "6", "1"]:
            found = True
            print(tickets[i])

    if not found:
        print('-1')
        exit(-1)


find_num_of_tickets()


