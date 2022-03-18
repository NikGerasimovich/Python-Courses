# Implement a Counter class which optionally accepts the start value and the counter stop value.
# If the start value is not specified the counter should begin with 0.
# If the stop value is not specified it should be counting up infinitely.
# If the counter reaches the stop value, print "Maximal value is reached."
# Implement to methods: "increment" and "get"
# * <em>If you are familiar with Exception rising use it to display the "Maximal value is reached." message.</em>
# startIn, stopIn = int(input("Введите начальное значение:")), int(input("Введите  конечное значение:"))


class Counter:

    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def increment(self):
        if self.start is None:
            self.start = 0

        if self.stop is not None and self.start <= self.stop:
            self.start += 1
        elif self.stop is None:
            Counter.outcnt += 1
        elif self.stop == 0:
            self.start += 1

    def get(self):
        if self.start > self.stop != 0:
            print("Достигнуто предельное значение")
        else:
            print(self.start)


c = Counter(start=None, stop=0)
c.increment()
c.get()
c.increment()
c.get()
c.increment()
