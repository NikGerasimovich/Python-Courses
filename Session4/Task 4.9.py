# Task 4.9
# Implement a bunch of functions which receive a changeable number of strings and return next parameters:
# 1) characters that appear in all strings
# 2) characters that appear in at least one string
# 3) characters that appear at least in two strings
# 4) characters of alphabet, that were not used in any string
# Note: use `string.ascii_lowercase` for list of alphabet letters
import string

inp_string = input("Введите строку: ")


def symb_on_all_str(inp_string):  # 1
    # Функция выводит символы, которые встречаются во всех строках

    start_string = str(inp_string).split()

    symb_on_2str = list()
    symb_all_wrd = list()

    # Поиск общих символов в первых двух словах
    for sec_word in start_string[1]:
        for frs_word in start_string[0]:
            if sec_word == frs_word:
                symb_on_2str.append(frs_word)

    # Поиск общего символа во всех строках, т.к он есть в первых двух строках
    for all_word in start_string[2::]:
        for symbol in all_word:
            for all_symbol in symb_on_2str:
                if symbol in all_symbol:
                    symb_all_wrd.append(symbol)
    if len(symb_all_wrd) < 1:
        return print("Таких символов нет")
    symb_all_wrd = set(symb_all_wrd)

    return print("Символы которые встречаются во всех строках: ", symb_all_wrd)


def symb_on_one_str(inp_string):  # 2
    # Функция выводит символы, которые встречаются хотя бы в одной строке

    start_string = str(inp_string).split()
    out_str = list()

    for i in start_string:
        for j in i:
            out_str.append(j)

    out_str.sort()
    out_str = set(out_str)

    return print("Символы которые встречаются хотя бы в одной в строчке: ", out_str)


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
    return print("Символы которые встречаются хотя бы в двух строчках: ", a)


def symb_not_in_str(inp_string):  # 4
    # Функция выводит все символы которые не присуствуют в строке
    all_symb = list(string.ascii_lowercase)
    for i in list(inp_string):
        for j in all_symb:
            if i == j:
                all_symb.remove(j)
                break

    return print("Символы которые не присуствуют в строке: ", all_symb)


symb_on_all_str(inp_string)
symb_on_one_str(inp_string)
symb_on_2plus_str(inp_string)
symb_not_in_str(inp_string)
