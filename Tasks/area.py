import math


def circle(r):
    return math.pi * r ** 2


def rectangle(a, b):
    return a * b


def triangle(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


choice = input("Площадь чего Вас интересует: 1-круг, 2-прямоугольник, 3 - треугольник: ")
if choice == '1':
    r = int(input("Введите радиус круга: "))
    s = circle(r)
    print(f"Площадь круга с радиусом {r} равна {s}")
elif choice == '2':
    a = int(input("Введите длину прямоугольника: "))
    b = int(input("Введите ширину прямоугольника: "))
    s = rectangle(a, b)
    print(f"Площадь прямоугольника с шириной {b} и длинной {a} равна {s}")
elif choice == '3':
    a = int(input("Введите первую сторону треугольника: "))
    b = int(input("Введите вторую сторону треугольника: "))
    c = int(input("Введите третью сторону треугольника: "))
    s = triangle(a, b, c)
    print(f"Площадь треугольника со сторонами {a},{b},{c} равна {s}")
