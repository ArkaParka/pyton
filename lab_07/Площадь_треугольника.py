import math

print("Выберете способ расчета площади: ")
print("1. Через длины сторон  a,b,c.")
print("2. Через координаты вершин A,B,C.")
a = float(input("Способ = "))

if a == 1:
    print("Введите длины сторон a,b,c")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('S =', s)

elif a == 2:
    print("Введите координаты вершин A,B,C")
    A = [0, 0]
    B = [0, 0]
    C = [0, 0]
    A[0], A[1] = map(int, input().split())
    B[0], B[1] = map(int, input().split())
    C[0], C[1] = map(int, input().split())
    s = math.fabs((A[1] - A[0]) * (C[1] - A[1]) - (C[0] - A[0]) * (B[1] - A[1])) / 2
    print('S =', s)

else:
    print("Неправильно введенные значения")
