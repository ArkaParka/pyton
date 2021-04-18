g = 9.8
print('Введите значения для x, v, t: ')
x = float(input("x_0 = "))
v = float(input("v_0 = "))
t = float(input("t = "))
x_t = x + v * t - (g * pow(t, 2)) / 2
print('x(t) = ', x_t)
