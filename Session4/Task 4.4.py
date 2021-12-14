# Task 4.4
# Implement a function `split_by_index(s: str, indexes: List[int]) -> List[str]`
# which splits the `s` string by indexes specified in `indexes`. Wrong indexes
# must be ignored.
# Examples:
# split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
# ["python", "is", "cool", ",", "isn't", "it?"]
#  split_by_index("no luck", [42])
# ["no luck"]
import string

inp_string = str(input())
numb_of_index = [int(i) for i in input("Введите нужные индексы через пробел:").split()]
dict_index = dict.fromkeys(numb_of_index)


def split_index(inp_string, dict_index):
    # Функция разбивает строку по введённую пользователям по индексам которые определяет тоже пользователь

    a = 0
    cut_string = tuple()


    for i in range(len(inp_string)):

        for j in dict_index:
            if i == j:
                sep_string = ''.join(inp_string[a:j])
                cut_string = cut_string + (sep_string,)
                a = j

    tmp = list(dict_index.keys())[-1]
    last_key = tmp
    cut_string = cut_string + (inp_string[last_key:],)
    cut_string = list(cut_string)

    return cut_string


print(split_index(inp_string, dict_index))

# !!!!!!!!!!Доделать проверку на неправильные индексы(if index > len(inp_data) return inp_data )!!!!!!!!!!!!!!!!!!!

# Функция проходит по строке и словарю, где ключи словаря это индексы введенные пользователем.
# Далее она делает срез от начала до превого индекса и значение запис в кортеж(потому что он не изменяемый),
# после она делает срез от индеска предьидущего символа к следующему индексу. В конце все записывается в список(по условию)