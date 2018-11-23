# Assuming h() returns an int
from module1 import h


def f():
    return 0


def g():
    return f(), 'foo', h()


x = g()  # x is a Tuple[int, str, int]

x.count()  # count
x[0].bit_length()  # bit_length
x[1].find()  # find
x[2].bit_length()  # bit_length
