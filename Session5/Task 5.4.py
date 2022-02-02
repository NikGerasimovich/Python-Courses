# Task 5.4
# Look through file `modules/legb.py`.
# 1) Find a way to call `inner_function` without moving it from inside of `enclosed_function`.
# 2.1) Modify ONE LINE in `inner_function` to make it print variable 'a' from global scope.
# 2.2) Modify ONE LINE in `inner_function` to make it print variable 'a' form enclosing function.


a = "I am global variable!"


def enclosing_func():
    a = "I am variable from enclosed function!"

    def inner_func():
        a = "I am local variable!"
        print(a)

    inner_func()  # Вызов ф-ции inner для вывода локальной переменной
    print(a)


enclosing_func()  # Вызов ф-ции enclosing для вывода нелокальной области(охватывающей) переменной
print(a)  # Вызов глобальной переменной
