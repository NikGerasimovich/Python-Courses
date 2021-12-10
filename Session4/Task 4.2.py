# Task 4.2 Write a function that check whether a string is a palindrome or not. Usage of any reversing functions
# is prohibited. To check your implementation you can use strings from [here](
# https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).

polindrom = str(input())


def polindrom_doubl(polindrom):
    # Фун-ия вычисления полиндрома. Слово будет проверяться по середине. Если первая часть(допустим слово топот) ==
    # второй части(в перевернутом виде)тогда выведет True, иначе False

    tmppol = polindrom
    if len(tmppol) % 2 == 0:
        halfpolindrom1 = polindrom[:(len(polindrom) // 2)]
        halfpolindrom2 = polindrom[len(polindrom) // 2:]
    else:
        halfpolindrom1 = polindrom[:(len(polindrom) // 2) + 1]
        halfpolindrom2 = polindrom[len(polindrom) // 2:]

    halfpolindrom2 = list(halfpolindrom2)
    halfpolindrom2 = halfpolindrom2[::-1]
    halfpolindrom2 = ''.join(halfpolindrom2)
    halfpolindrom3 = halfpolindrom2

    if halfpolindrom1 == halfpolindrom3:
        return print("Это полиндром:", polindrom)
    else:
        return print("Это не полиндром:", polindrom)

polindrom_doubl(polindrom)
"""
def revers_polindrom(halfpolindrom2):
    polindrom_doubl(polindrom)
    global halfpolindrom3
    halfpolindrom2 = list(halfpolindrom2)
    halfpolindrom2 = halfpolindrom2[::-1]
    halfpolindrom2 = ''.join(halfpolindrom2)
    halfpolindrom3 = halfpolindrom2

    return halfpolindrom3


def calc_polindrom(halfpolndrom1, halfpolindrom3):
    polindrom_doubl(polindrom)

    if halfpolndrom1 == halfpolindrom3:
        return print("Это полиндром:", polindrom)
    else:
        return print("Это не полиндром:", polindrom)
"""

