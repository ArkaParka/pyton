def power_of_two(n):
    count = 0
    while 2**count <= n:
        count += 1
    return count


n = int(input("Введите число: "))
print(power_of_two(n))