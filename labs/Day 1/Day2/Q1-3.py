# Iterator

class MyIterator:
    def __init__(self):
        self.i = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= 3:
            self.i += 1
            return self.i - 1
        raise StopIteration

for x in MyIterator():
    print(x)
    
    
#Generator

def my_generator():
    for i in range(1, 5):
        yield i

for x in my_generator():
    print(x)