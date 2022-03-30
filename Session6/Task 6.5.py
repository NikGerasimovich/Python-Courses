# Task 6.4 A singleton is a class that allows only a single instance of itself to be created and gives access to that
# created instance. Implement singleton logic inside your custom class using a method to initialize class instance.


class ClassicSingelton(object):
    """ Реализация классического класса Singleton"""

    def __new__(cls):  # Метод для управления созданием обьекта
        if not hasattr(cls, "instance"):  # Метод hashttr позволяет определить есть ли у обьекта определенное свойство
            cls.instance = super(ClassicSingelton, cls).__new__(cls)
        return cls.instance


p = ClassicSingelton()
v = ClassicSingelton()
print("Классический Singelton \n", p, "\n", v, "\n", p is v)


# С помощью метода hassatr осуществляется проверка налчие у обьекта cls свойства instance. В данном случае при
# создании нового обьекта v hasattr обнаруживает, что у обьекта уже существует свойство instance , и использует уже
# существующий(созданный экземпляр)


class DefInstSingelton:
    """Реализация отложенного экзмепляра Singelton"""
    _instance = None

    def __init__(self):
        if not DefInstSingelton._instance:
            print("_init_ method called....")
        else:
            print("Instance already created:", self.getInstance())

    @classmethod        # Метод класса имеющий доступ ко всем атрибутом класса через который он был вызван
    def getInstance(cls):
        if not cls._instance:
            cls._instance = DefInstSingelton()
        return cls._instance


p1 = DefInstSingelton()
p1.getInstance()
v1 = DefInstSingelton()
v1.getInstance()
print("\nОтложенный экзмепляр Singelton \n", p1, "\n", v1, "\n", p1 is v1)

# Отложенное создание экземпляра класса нужен для создание обьекта только тогда, когда он действительно нужен. При
# вызове класса DefInstSingelton() вызывается метод _init_() , но сам обьект создаться только при использование
# метода DefInstSingelton.getInstance()
