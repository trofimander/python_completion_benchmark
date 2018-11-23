# Assuming h() returns instance of E
from module1 import e


class C:
    def foo(self):
        pass


class D:
    def bar(self):
        pass


def f():
    return C


a = f()
b = D()
c = e()

a.foo(C())  # foo
b.bar()  # bar
c.baz()  # baz
