print("Даниленко Кірілл Артурович \nЛабораторна робота №1 \nВаріант 2 \nОбчислення відсотку від числа \n")
import re
def myfunc():

    xa = float(re.search(r'[+-]?([0-9]*[.])?[0-9]+',input("Введите координату x для А: ")).group())
    ya = float(re.search(r'[+-]?([0-9]*[.])?[0-9]+',input("Введите координату y для A: ")).group())
    xb = float(re.search(r'[+-]?([0-9]*[.])?[0-9]+', input("Введите координату x для B: ")).group())
    yb = float(re.search(r'[+-]?([0-9]*[.])?[0-9]+', input("Введите координату y для B: ")).group())


    sumA = abs(xa) + abs(ya)
    sumB = abs(xb) + abs(yb)

    if sumA == sumB:
        print("Точки находятся на одном отдалении")
    else:
        if sumA < sumB:
            print("Точка А ближе к началу координат")
        else:
            print("Точка B ближе к началу координат")

    c = input("Продолжить тестирование программы? Y/N")
    if c == 'Y' or c == 'y':
        myfunc()
    else:
        return()

myfunc()
