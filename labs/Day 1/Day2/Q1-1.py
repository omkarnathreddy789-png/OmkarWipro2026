class Num:
    def __init__(self, n):
        self.n = n
        self.i = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= self.n:
            self.i += 1
            return self.i - 1
        raise StopIteration

for x in Num(10):
    print(x)
