from itertools import count, takewhile


def fib():
    a, b = 1, 0
    while(True):
        a, b = a + b, a
        yield a


print sum(filter(lambda y: not y % 2, takewhile(lambda x: x <= 4000000, fib())))
