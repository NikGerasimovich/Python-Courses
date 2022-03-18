# Implement custom dictionary that will memorize 10 latest changed keys. Using method "get_history" return this keys.
# <em>After your own implementation of the class have a look at collections.deque
# https://docs.python.org/3/library/collections.html#collections.deque </em>
from collections import deque


class HistoryDict:
    keychangelist = deque(list(), 10)

    # keychangelist = list()

    def __init__(self, first_dict):
        self.first_dict = first_dict

    def set_value(self, keychange, val):
        self.keychange = keychange
        self.keychangelist.append(self.keychange)
        # self.keychangelist = self.keychange
        # if len(self.keychangelist) > 10:
        #   self.keychangelist.pop(0)

    def get_history(self):
        print(self.keychangelist)


d = HistoryDict({"foo": 42})
d.set_value("1", 21)
d.set_value("2", 21)
d.set_value("3", 21)
d.set_value("4", 21)
d.set_value("5", 21)
d.set_value("6", 21)
d.set_value("7", 21)
d.set_value("8", 21)
d.set_value("9", 21)
d.set_value("10", 21)
d.set_value("11", 21)
d.set_value("12", 21)

d.get_history()

# Отличие обычного варианта и использование deque в том, что в deque можно сразу задать длину и он будет
# автоматически обрезать длину списка до 10(по усл)
