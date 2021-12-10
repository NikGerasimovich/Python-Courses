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
    dict_remove = {" ": "", ",": "", ":": "", "-": "", "'": "", '"': ""}

    if separator != "" and separator == 0:
        for i in inp_string:
            for j in dict_remove:
                if i == j and j == separator:
                    inp_string = inp_string.replace(i, "")

    elif separator !="" and max_split != 0:
        for i in inp_string:
            for j in dict_remove:
                if i == j and j == separator:
                    sep = inp_string.find(separator)
                    inp_string = "".join(inp_string[:sep])

                    #Не работает сепаратор
    else:
        for i in inp_string:
            inp_string = inp_string.replace(" ", '')


    inp_string = list(inp_string)

    return inp_string

print(my_split(inp_string, separator, max_split))