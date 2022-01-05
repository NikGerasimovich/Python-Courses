# Task 5.1 Open file `data/unsorted_names.txt` in data folder. Sort the names and write them to a new file called
# `sorted_names.txt`. Each name should start with a new line as in the following example: Adele Adrienne .... Willodean
# Xavier

import string

out_file = open('Sort Names for task 5.1.txt', 'w+')

for letter in string.ascii_uppercase:  # string.ascii_uppercase - это алфавит A-Z
    with open('Names for Task 5.1.txt', 'r') as inp_file:
        for symb in inp_file:
            if symb[0] == letter:
                out_file.writelines(symb)
out_file.close()

# Первый цикл проходит по алфавиту а второй по всему файлу забираю из него первую строку with open('Names for Task
# 5.1', 'r') as inp_file: нужна для постоянного закрытия файла и открытия заново для обращения к следующей строчке,
# этот метод делает это автоматически
# !!!!!!!!!!!!!!! Есть баг на именах Oma и Penny их не разбивает !!!!!!!!!!!
