print("Даниленко Кірілл Артурович \nЛабораторна робота №1 \nВаріант 2 \nОбчислення відсотку від числа \n")
import re
def myfunc():

        a = float(re.search(r'[+-]?([0-9]*[.])?[0-9]+',input("Введите число a: ")).group())
        b = float(re.search(r'[+-]?([0-9]*[.])?[0-9]+',input("Введите число b: ")).group())

        if a > 0 and b > 0:
            print((b / a) * 100)
            c = input("Продолжить тестирование программы? Y/N")
            if c == 'Y' or c == 'y':
                myfunc()
            else:
                return
        else:
            print("Введите положительные числа!")
            myfunc()

myfunc()
