print("Даниленко Кірілл Артурович \nЛабораторна робота №2 \nВаріант 2 \nОбчислення суми \n")
import re
def whole_func():

    upper_border = int(re.search(r'[+-]?\d+', input("Введите верхнюю границу суммы (>=1): ")).group())
    if upper_border <1:
        print("Введите данные корректно!")
        whole_func()


    func_argument = float(re.search(r'[+-]?([0-9]*[.])?[0-9]+', input("Введите значение аргумента функции: ")).group())
    if func_argument == 0:
        print("Введите ненулевой аргумент функции!")
        func_argument = float(re.search(r'[+-]?([0-9]*[.])?[0-9]+', input("Введите значение аргумента функции: ")).group())


    total_sum = 0
    for down_border in range(upper_border):

        total_sum = total_sum + down_border/(func_argument**down_border)
    print(total_sum)

    c = input("Продолжить тестирование программы? +/-")
    if c == '+':
        whole_func()
    else:
        return ()
whole_func()
