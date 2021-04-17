s, l1, r1, l2, r2 = map(int, input("Введите данные: ").split())

if l1 > r1 or l2 > r2:
    print("Неверно введенные данные")

s1 = r1 - l1
s2 = r2 - l2

probable_x2 = s - l1

if probable_x2 < l2:
    distance_to_left = l2 - probable_x2
    if distance_to_left <= s1:
        x1 = l1 + distance_to_left
        x2 = l2
        print(x1, x2)
    else:
        print(-1)
elif probable_x2 > r2:
    distance_to_right = probable_x2 - r2
    if distance_to_right <= s1:
        x1 = l1 + distance_to_right
        x2 = r2
        print(x1, x2)
    else:
        print(-1)
else:
    print(l1, probable_x2)
