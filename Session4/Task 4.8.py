# Task 4.8
# Implement a function `get_pairs(lst: List) -> List[Tuple]` which returns a list
# of tuples containing pairs of elements. Pairs should be formed as in the
# example. If there is only one element in the list return `None` instead.
# Example:
# get_pairs([1, 2, 3, 8, 9])
# [(1, 2), (2, 3), (3, 8), (8, 9)]
# get_pairs(['need', 'to', 'sleep', 'more'])
# [('need', 'to'), ('to', 'sleep'), ('sleep', 'more')]


inp_lst = [i for i in input("Введите нужные индексы через пробел:").split()]


def get_pairs(inp_lst):
    # Функция состовляющая пары входных значений

    inp_dct = {}
    cnt = 0
    out_pairs = tuple()
    lst1 = list()

    for i in inp_lst:
        cnt += 1
        if len(inp_lst) == 1:
            return None
        elif cnt in range(len(inp_lst)):
            inp_dct[i] = inp_lst[cnt]
        else:
            break

    for item in inp_dct.items():
        out_pairs = out_pairs + (item,)
        lst1.extend(out_pairs)
        out_pairs = tuple()

    return lst1


print(get_pairs(inp_lst))

# Функция переводит вх список в словарь и состовляет значения по парам за исключ последнего значения
# Затем она переводит словарь в кортеж и добовляет его в список(См усл)
