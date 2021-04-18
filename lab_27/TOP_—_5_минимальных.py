def sort_signals(arr, element):
    arr.append(element)
    j = len(arr) - 2
    while j >= 0 and arr[j] < element:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = element


n = int(input("Введите число сигналов: "))

if not 1 <= n <= 100000:
    print('Неверное количество чисел')
    exit(-1)

signals = list(map(int, input('Массив сигналов: ').split(' ')))
visible = []

for signal in signals:
    sort_signals(visible, signal)
    visibleLen = len(visible)
    print(*visible[-5:])
