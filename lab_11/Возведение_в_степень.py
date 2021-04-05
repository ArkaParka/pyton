num = int(input("Введите число: "))
pow = int(input("Введите степень: "))

tempNum = num
while pow > 1:
    pow = pow - 1
    num = tempNum * num

print("Результат: ", num)