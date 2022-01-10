# Task 5.2
# Implement a function which search for most common words in the file.
# Use `data/lorem_ipsum.txt` file as a example.
# python
# def most_common_words(filepath, number_of_words=3):
#    pass
# print(most_common_words('lorem_ipsum.txt'))
# >>> ['donec', 'etiam', 'aliquam']
# > NOTE: Remember about dots, commas, capital letters etc.


number_of_words = int(input('Введите количество слов: '))
file = 'lorem_ipsum.txt'


def most_common_words(file, number_of_words):
    # Функция поиска часто повторяющихся слов в тексте
    from collections import Counter
    with open(file, 'r') as text:
        text1 = text.read()
        text1 = text1.split()
        Counter = Counter(text1)
        most_word = Counter.most_common(number_of_words)
        return print(most_word)


most_common_words(file, number_of_words)

# Функция принимает на вход текстовый файл и количество слов на вывод После чтения текста он превращается в строку
# которую можно разбить split-ом на отдельные слова. Далее с помощью библиотеки collections вызывается Counter
# которые ведёт подсчёт хэшируемых обьектов и на выход даёт словарь. С помощью most_word = Counter.most_common(
# number_of_words) на выход функции поступает список словарей количеством равнным количеству слов заданных с консоли
