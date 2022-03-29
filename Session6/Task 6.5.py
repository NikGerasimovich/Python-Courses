# Task 6.4 A singleton is a class that allows only a single instance of itself to be created and gives access to that
# created instance. Implement singleton logic inside your custom class using a method to initialize class instance.


class Inst(object):
    """ Реализация класса Singleton"""

    def __new__(cls):  # Метод для управления созданием обьекта
        if not hasattr(cls, "instance"):  # Метод hashttr позволяет определить есть ли у обьекто определенное свойство
            cls.instance = super(Inst, cls).__new__(cls)
        return cls.instance


p = Inst()
v = Inst()

print(p is v)
print(p)
print(v)

# С помощью метода hassatr осуществляется проверка налчие у обьекта cls свойства instance. В данном случае при
# создании нового обьекта v hasattr обнаруживает, что у обьекта уже существует свойство instance , и использует уже
# существующий(созданный экземпляр)
