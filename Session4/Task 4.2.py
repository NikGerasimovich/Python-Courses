### Task 4.2
##Write a function that check whether a string is a palindrome or not. Usage of any reversing functions is prohibited. To check your implementation you can use
##strings from [here](https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).

polindrom = str(input())
polindromglobal = list(polindrom)
def polindrom_calc(polindrom):
#Фун-ия вычисления полиндрома.
# Слово будет проверяться по середине. Если первая часть(допустим слово топот) == второй части(в перевернутом виде)тогда выведет True, иначе False
    tmppol = polindrom
    if len(tmppol) % 2 == 0:
        global polindromglobal
        halfpolindrom1 = polindrom[len(polindrom)//2 + 1:]
        halfpolindrom2 = polindrom[len(polindrom)//2:]



        return print(halfpolindrom1, halfpolindrom2)

polindrom_calc(polindrom)