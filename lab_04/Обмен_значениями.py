print('Введите два числа: ')
a = int(input("a = "))
b = int(input("b = "))
temp = a
a = b
b = temp
print('a =', a, ',b =', b)
a, b = b, a
print('a =', a, ',b =', b)
