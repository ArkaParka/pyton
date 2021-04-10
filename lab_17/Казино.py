import collections

def casino():
    k = 1
    dropped_numbers = []
    red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    black_numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    red_count = 0
    black_count = 0
    while True:
        n = int(input('Введите число: '))
        if n <= 0 or n > 36:
            exit(0)
        if len(dropped_numbers) > 12:
            dropped_numbers.pop(0)
        dropped_numbers.append(n)

        print('Список номеров выпадающих чаще всего ', *frequently_used(dropped_numbers), sep=" ")

        print(f'Список номеров НЕ выпавших за последние {k} игр:')
        for i in range(1, 37):
            if not dropped_numbers.__contains__(i):
                print(i, end=" ")
        print(" ")

        if red_numbers.__contains__(n):
            red_count += 1
        elif black_numbers.__contains__(n):
            black_count += 1
        print('Количество красных: ', red_count, ',количество черных: ', black_count)
        print(" ")
        k += 1


def frequently_used(arr):
    arr = collections.Counter(arr).most_common()
    temp_arr = []
    max_item = arr[0][1]
    for i in arr:
        if i[1] > max_item:
            max_item = i[1]
    for item in arr:
        if item[1] == max_item:
            temp_arr.append(item[0])
    return temp_arr


casino()
