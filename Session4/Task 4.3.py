# Task 4.3
# Implement a function which works the same as `str.split` method
# (without using `str.split` itself, ofcourse).

inp_string = str(input())
separator = input("Введите сепартор:")
while True:
    try:
        max_split = int(input("Введите количество разбиений: "))
        break
    except ValueError:
        print("Ввдети число, если разбивать не нужно введте 0")


def my_split(inp_string, separator, max_split):
    #Функция которая заменяет метод .split для любого сепаратора и значений max_split 0 либо 1

    dict_remove = {" ": "", ",": "", ":": "", "-": "", "'": "", '"': ""}

    if separator != "" and max_split == 0:
        for i in inp_string:
            for j in dict_remove:
                if i == j and j == separator:
                    inp_string = inp_string.replace(i, "")

    elif separator != "" and max_split != 0:
        for i in inp_string:
            for j in dict_remove:
                if i == j and j == separator:
                    sep = inp_string.find(separator)
                    sep_string = ''.join(inp_string[:sep])

    else:
        for i in inp_string:
            inp_string = inp_string.replace(" ", '')

    out_string = list()
    out_string.append(sep_string)
    out_string.append(inp_string[(sep+1):])

    return out_string


print(my_split(inp_string, separator, max_split))

# Програма выполняет работы метода .split но только для значений max_split = 0 либо 1
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Надо доработать !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!