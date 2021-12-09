### Task 4.1
## Implement a function which receives a string and replaces all `"` symbols with `'` and vise versa.
import re
inp_string = str(input())


def rec_quotes(inp_string):
##Функция предназначена для замены " на ' и в обратном порядке
    teststr = str()
    for i in inp_string:
        if i == '"':
            teststr = inp_string.replace('"', "'")
        elif i == "'":
            teststr = inp_string.replace("'", '"')
    return teststr


print(rec_quotes(inp_string))

## В функция приходит строка, где с помощью функции replace происходит замена одного символа на другой
