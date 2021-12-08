### Task 1.3
##Create a program that asks the user for a number and then prints out a list of all the [divisors](https://en.wikipedia.org/wiki/Divisor) of that number.
##Examples:
##Input: 60
##Output: {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}

num = int(input())
lst = []
for i in range(num):
    if i > 0 and not (num % i):
        mun = num // i
        lst.append(mun)

lst.reverse()
print(lst)

## Цикл идёт по всему промежутку знач с условием что делители не будут браться которые делять с остатком