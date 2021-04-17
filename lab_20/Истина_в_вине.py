class DefineAlko:
    def __init__(self, name, price, capacity):
        self.name = name
        self.price = int(price)
        self.v = int(capacity)


def input_data(length):
    alko_arr = []
    alko_v_arr = []
    for _ in range(length):
        data = input().split(' ')
        alko = DefineAlko(*data)
        alko_arr += [alko]
        alko_v_arr += [alko.v * (money // alko.price)]
    return [alko_arr, alko_v_arr]


money = int(input('Количество денег: '))
length = int(input('Количество алкоголя: '))

data = input_data(length)
alko_arr = data[0]
alko_v_arr = data[1]

max_v = max(alko_v_arr)
target = alko_arr[alko_v_arr.index(max_v)]

n = money // target.price

if not n:
    print(-1)
else:
    print(target.name, n)
    print(n * target.v)
    print(money - n * target.price)
