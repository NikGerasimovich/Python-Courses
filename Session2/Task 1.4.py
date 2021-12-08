##Write a Python program to sort a dictionary by key.
import random

dct_tst = {"A": 5,
           "B": "kjkj",
           "C": 686,
           "D": 345}
lst = []
for x in dct_tst:
    lst.append(x)

print("Only keys:", *lst, sep=' \n')

## Сортировка словаря, на выходе выдаются только ключи