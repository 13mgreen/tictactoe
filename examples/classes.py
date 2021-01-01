class Counter:
    def __init__(self, initial_value=0):
        self.count = initial_value

    def increment(self):
        self.count += 1

    def print_counter(self):
        print(self.count)

    def decrement(self):
        if self.count > 0:
            self.count -= 1
        else:
            print("Can't decrement")


c = Counter()

c.increment()
c.increment()
c.increment()
c.increment()
c.decrement()
c.print_counter()

lame_counter = Counter(20)


lame_counter.decrement()
lame_counter.decrement()
lame_counter.decrement()
lame_counter.decrement()
lame_counter.decrement()
lame_counter.decrement()
lame_counter.decrement()
lame_counter.print_counter()