# Task 4.5
# Implement a function `get_digits(num: int) -> Tuple[int]` which returns a tuple of a given integer's digits.
# Example:
# split_by_index(87178291199)
# (8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)

print("Данная программа разбивает число на части по одному элементу")
while True:
    try:
        inp_digits = int(input("Введите число:  "))
        break
    except ValueError:
        print("Вы ввели не числовые значения!!!")


def get_diits(inp_digits):
    cahnge_dig = str(inp_digits)
    outp = tuple()
    for i in cahnge_dig:
        outp = outp + (i,)

    return outp


print(get_diits(inp_digits))

# Программа проверяет введено ли число и дальше переводит его в строку и проходя по строке доб кажд эл-т в кортеж
