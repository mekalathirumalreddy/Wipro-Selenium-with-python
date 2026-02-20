'''#1.Create a custom iterator that prints numbers from 1 to 5.

iterator=iter(range(1,6))
for i in range(5):
    print(next(iterator))


#2.Write an iterator class that returns next even number.
iterator=iter(range(0,10))
print(next(iterator))'''


#1
class Numbers:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 5:
            value = self.num
            self.num += 1
            return value
        else:
            raise StopIteration


obj = Numbers()
for i in obj:
    print(i)

#2

class EvenIterator:
    def __init__(self):
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.num += 2
        return self.num


even = EvenIterator()
for i in range(5):
    print(next(even))


#3
class DemoIterator:
    def __init__(self):
        self.x = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.x <= 3:
            value = self.x
            self.x += 1
            return value
        else:
            raise StopIteration


demo = DemoIterator()
for i in demo:
    print(i)


#1

def numbers(n):
    for i in range(1, n + 1):
        yield i


for i in numbers(5):
    print(i)

#2

def even_numbers(n):
    for i in range(2, n + 1, 2):
        yield i


for i in even_numbers(10):
    print(i)

#3

def read_file(filename):
    with open(filename, "r") as f:
        for Line in f:
            yield line


for line in read_file("data.csv"):
    print(line)

#4

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


for i in fibonacci(7):
    print(i)


#5

def retry():
    for attempt in range(1, 4):
        yield f"Attempt {attempt}"


for i in retry():
    print(i)

