# Task 4.10 Implement a function that takes a number as an argument and returns a dictionary, where the key is a
# number and the value is the square of that number. print(generate_squares(5)) -> {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


inp_range = int(input("Введите значения через пробел: "))


def square(inp_range):
    # Функция возводит в квадрат ключи и формирует новый словарь из клч и знач
    inp_lst = list(range(1, inp_range+1))
    inp_dict = dict.fromkeys(inp_lst)
    out_lst = list()

    for key in inp_dict:
        val = key * key
        out_lst.append(val)
    out_dict = {i: o for i, o in zip(inp_lst, out_lst)}

    return out_dict


print(square(inp_range))

# Функция возводит в квадрат ключи и затем записывает их в другой список
# С помощью функции zip формируется выходной словарь из ключей входных данных и значений - квадратов этих данных
