### Task 1.2
## Write a Python program to count the number of characters in a string (ignore case of letters).
##Examples:
##Input: 'Oh, it is python'
##Output: {',': 1, ' ': 3, 'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1}

str_for_test = input()
dicstr = dict.fromkeys(str_for_test, 0)

for i in str_for_test:
        dicstr[i] += 1

print(dicstr)

## Необходимо перевести строку в словарь. Далее цикл идёт по строке и прибавляет 1 в словаре где символы повторяются.
##Все символы это ключи