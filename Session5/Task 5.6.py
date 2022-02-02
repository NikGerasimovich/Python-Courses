# Task 5.6
# Implement a decorator `call_once` which runs a function or method once and caches the result.
# All consecutive calls to this function should return cached result no matter the arguments.
first_answ = list()


def decorator(func):
    def wrapper(a, b):
        first_answ.append(func(a, b))
        for i in first_answ:
            return print(i)
        return first_answ

    return wrapper


@decorator
def sum_of_numbers(a, b):
    return a + b


sum_of_numbers(6, 8)
sum_of_numbers(8, 8)
sum_of_numbers(1, 8)
sum_of_numbers(2, 8)
