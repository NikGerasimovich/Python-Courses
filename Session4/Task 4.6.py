# Task 4.6
# Implement a function `get_shortest_word(s: str) -> str` which returns the
# longest word in the given string. The word can contain any symbols except
# whitespaces (` `, `\n`, `\t` and so on). If there are multiple longest words in
# the string with a same length return the word that occurs first.
# Example:
# >>> get_shortest_word('Python is simple and effective!')
# 'effective!'

string = input("Please enter a string ")


def get_shortest_word(string):

    max_word = str()
    for word in string.split():
        if len(word) > len(max_word):
            max_word = word

    return print(max_word)


get_shortest_word(string)

# Строка разбивается split по словам и сравнивает длинну всех слов. Затем самое длинное выводится