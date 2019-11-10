print("Даниленко Кирилл Артурович\nЛабораторная работа №4 \nВариант 2 \nСравнение площадей треугольников\n")
def my_program():

    splitted_sentence = input("Введите предложение: ").split()
    word_index = 0
    join_sign = " "
    while word_index < len(splitted_sentence):
        if len(splitted_sentence[word_index]) == 5:
            splitted_sentence[word_index] = splitted_sentence[word_index][:-2] + "xz";
        word_index += 1

    print("Новое предложение: ", join_sign.join(splitted_sentence))
    keep_running = input("Продолжить тестирование программы? +/-")
    if keep_running == "+":
        my_program()
    else:
        return ()
my_program()