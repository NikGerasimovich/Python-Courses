# File `data/students.csv` stores information about students in [CSV](
# https://en.wikipedia.org/wiki/Comma-separated_values) format. This file contains the student’s names,
# age and average mark.
import csv

file_path = "students.csv"
number_of_student = int(input("Введите количество студентов: "))


def get_list(file_path, number_of_student):
    # Функция парсинга из файла csv. и обработки значений имён и оценок с выводом лучших учеников по вводу пользователя
    with open(file_path) as csv_file:
        csv_read = csv.reader(csv_file, delimiter=',')
        out_list = list()
        # Парсинг из файла и добовление в 2 списка имён и оценок и создание словаря где ключ - имя , а значение - оценка
        dict_of_students = {row[0]: row[2] for row in csv_read if row[0] != 'student name'}
        # Сортировка словоря по значением, где grade[0] это обозначение кортежа в случаи если оценка одинаковая то
        # сортировка пройдёт по ключу
        for val in sorted(dict_of_students.items(), key=lambda grade: (grade[1], grade[0]), reverse=True):
            out_list.append(val)
        return out_list[:number_of_student]


def oldest_student(file_path):
    # Функция сортирует учеников по возрасту и записывает в новый csv-файл начиная с самых старших
    with open(file_path, mode='r') as csv_file:
        csv_read = csv.DictReader(csv_file)
        out_list = list()
        # Запись списка словарей в виде 1 словарь = 1 строке файла csv
        for row in csv_read:
            out_list.append(row)
    with open('old_student.csv', mode='w', newline='') as csv_file_write:  # newline нужен для записи в каждую строку
        csv_file_writer = csv.writer(csv_file_write, delimiter=',')
        csv_file_writer.writerow(['student name', 'age', 'average mark'])  # Заголовок файла
        for step in sorted(out_list, key=lambda k: (k['age'], k['student name']),
                           reverse=True):  # Сортировка идёт по возрасту и если он == то по имени
            csv_file_writer.writerow([step['student name'], step['age'], step['average mark']])

    return


oldest_student(file_path)
best_students = get_list(file_path, number_of_student)
print(best_students)

# Функция 1. Осуществляет получение данных из csv файлы и сортировку по самой лучшей оценке и дальнейший вывод на
# экран. Пользователь задаёт количество учеников которых надо указать Функция 2. Осуществляет получение данных из csv
# файлы и сортировку по возрасту и дальнейшую запись всех учеников в той же форме что и в исходном файле в новый
# файл. Старые->Молодые
