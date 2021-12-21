# Task 4.7
# Implement a function `foo(List[int]) -> List[int]` which, given a list of
# integers, return a new list such that each element at index `i` of the new list
# is the product of all the numbers in the original array except the one at `i`.
# Example:
# >>> foo([1, 2, 3, 4, 5])
# [120, 60, 40, 30, 24]


foo_list = [int(i) for i in input("Введите нужные индексы через пробел:").split()]


def foo(foo_list):
    # Функция которая перемножает элементы между собой кроме того, на котором курсор

    lst1 = list()
    dct = dict.fromkeys(foo_list)
    for key in dct:
        val = 1
        for j in foo_list:
            val = j * val
            out_value = val
        if key > 1:
            out_value = out_value // key
        lst1.append(out_value)

    return print(lst1)


foo(foo_list)

# Функция добовляет список в словарь и дальше идёт по ключам и значениям списка
# Значения списка и словаря одинаковые. В конце цикла деление на ключ осущ для
# изьятия из результата элемента на которм курсор(Курсор/ключ = 2. 1*2*3*4*5=120 но 2 не учитыв. Итог 60)
