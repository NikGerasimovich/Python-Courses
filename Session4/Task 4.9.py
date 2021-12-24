# Task 4.9
# Implement a bunch of functions which receive a changeable number of strings and return next parameters:
# 1) characters that appear in all strings
# 2) characters that appear in at least one string
# 3) characters that appear at least in two strings
# 4) characters of alphabet, that were not used in any string
# Note: use `string.ascii_lowercase` for list of alphabet letters
import string

inp_string = input("Введите строку: ")

def symb_on_all_str(inp_string):  # 3
    # Функция выводит символы которые встречаются как минимум в двух строках
    sec_word = str(inp_string)
    a = list()
    for i in sec_word:
        if sec_word.count(i) > 2:
            a.append(i)

    return print(a)
symb_on_all_str(inp_string)


def symb_on_2plus_str(inp_string):  # 3
    # Функция выводит символы которые встречаются как минимум в двух строках
    sec_word = str(inp_string)
    a = list()
    for i in sec_word:
        if sec_word.count(i) != 1:
            if i == " ":
                break
            else:
                a.append(i)
    a = set(a)
    return print(a)


def symb_not_in_str(inp_string):  # 4
    # Функция выводит все символы которые не присуствуют в строке
    all_symb = list(string.ascii_lowercase)
    for i in list(inp_string):
        for j in all_symb:
            if i == j:
                all_symb.remove(j)
                break

    return all_symb
