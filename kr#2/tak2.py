# 2 задание 5 варианта

class ShapeIterator:
    def __init__(self, n):
        self.n = n
        self.st = '/'
        self.array = ['/'] * (n+1)
        self.lenght = len(self.array)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < self.n:
            if self.n % 2 == 0:
                a = self.array[self.index % self.lenght]
                self.index += 1
            return a * self.n
        else:
            a = self.array[self.index % self.lenght//2 + 1]
            a = a * self.index
            self.index += 1
            return a


for i in ShapeIterator(4):
    print(i)
