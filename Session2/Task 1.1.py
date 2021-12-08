## Task 1.1
##Write a Python program to calculate the length of a string without using the `len` function.

str_test = "This_is_test_func_with_out_length"
count = 0
for i in str_test:
    count += 1
print(count)
print(len(str_test)) ##Для проверки

## Цикл идёт по элементам строки и мы воводим значение счетчика то есть и есть значение метода len()