print("Даниленко Кірілл Артурович \nЛабораторна робота №2 \nВаріант 2 \nВидалення цифри з натурального числа\n")
import re
def whole_func():

    natural_number =  int(re.search(r'[+-]?\d+', input("Введите натуральное число: ")).group())
    remove_char = int(re.search(r'[+-]?\d+', input("Введите цифру, которую нужно изъять из числа: ")).group())



    if natural_number <1 or remove_char <1 or natural_number < remove_char:
        print("Введите корректные числа!")
        whole_func()
    new_number = ''

    for iter_value in str(natural_number):
       if str(remove_char) != iter_value:
            new_number = new_number + iter_value
    print('Новое число: '+ new_number)

    c = input("Продолжить тестирование программы? +/-")
    if c == '+':
        whole_func()
    else:
        return ()

whole_func()
