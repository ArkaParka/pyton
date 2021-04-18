# вес в кг, рост в метрах.
# Возвращает индекс массы тела.
def bmi(weight: float, height: float) -> float:
    return weight / (height ** 2)


# Принимает численное значение ИМТ и печатает на экран соответствующую категорию
def print_bmi(bmi: float) -> float:
    if bmi < 18.5:
        res = 'Underweight'
    elif bmi < 25:
        res = 'Normal'
    elif bmi < 30:
        res = 'Overweight'
    else:
        res = 'Obesity'

    print(res)


w, h = map(float, input('Рост вес: ').split(' '))
h /= 100
print_bmi(bmi(w, h))
