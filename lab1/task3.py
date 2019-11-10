print("Даниленко Кірілл Артурович \nЛабораторна робота №1 \nВаріант 2 \nОбчислення виразу в залежності від значення \n")
import re
def myfunc():

    x = float(re.search(r'[+-]?([0-9]*[.])?[0-9]+', input("Введите значение x: ")).group())
    control_value = float(re.search(r'[+-]?([0-9]*[.])?[0-9]+', input("Введите контрольное значение: ")).group())

    if x >= control_value :
        print("x = %.4f" %(x**2 - 3*x +9))
        c = input("Продолжить тестирование программы? Y/N")
        if c == 'Y' or c == 'y':
            myfunc()
        else:
            return ()
    else:
        print("x = %.4f" %(1/(x**3-6)))
        c = input("Продолжить тестирование программы? Y/N")
        if c == 'Y' or c == 'y':
            myfunc()
        else:
            return ()
myfunc()