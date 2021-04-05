h1_m1 = input("Введите время: ").split(":")
h2_m2 = input("Введите время: ").split(":")

date1 = int(h1_m1[0], 10) * 60 + int(h1_m1[1], 10)
date2 = int(h2_m2[0], 10) * 60 + int(h2_m2[1], 10)

sub = date2 - date1
if sub < 0:
    sub * -1

if sub < 15:
    print("Встреча состоится")
else:
    print("Встреча не состоится")