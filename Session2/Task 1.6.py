### Task 1.6
## Write a Python program to convert a given tuple of positive integers into an integer.
##Examples:
##Input: (1, 2, 3, 4)
##Output: 1234

inp_data = (1, 2, 3, 4, 5)

print(int(''.join(map(str, inp_data))))

## с помощью join показывается какой элмент надо вставить/убрать при это метод map нужен для обращения к всем элементам
## + перевод в строку так как кортеж - не изменяемый