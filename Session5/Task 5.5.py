# Task 5.5 Implement a decorator `remember_result` which remembers last result of function it decorates and prints it
# before next call.

old_res = [0]

# Декоратор
def remember_result(func):
    def wrapper(*args, **kwargs):
        # В врапере каждое новое значение из sum_list сравнивается с old_res и записывается в old_res а старое удаляется
        for i in old_res:
            if i == 0:
                old_res.append(func(*args, **kwargs))
                old_res.remove(i)
                print("Last result: None")
                print("Current result", func(*args, **kwargs))
                break
            else:
                print("Last result: ", i)
                print("Current result: ", func(*args, **kwargs))
                old_res.remove(i)
                old_res.append(func(*args, **kwargs))
                break
        return func(*args, **kwargs)
    return wrapper


@remember_result
def sum_list(*args):
    result = ""
    for item in args:
        result += item

    return result


sum_list("hel", "lo")
sum_list("Ami", "ne")
sum_list("stu", "pid")
sum_list("1", "2")
sum_list("3", "4")
sum_list("5", "6")