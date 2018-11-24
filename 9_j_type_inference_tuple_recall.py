class C:
    def foo(self):
        pass


class D:
    def bar(self):
        pass


class E:
    def baz(self):
        pass


def f():
    return 0


def g():
    return


x = (C(), D(), E())

a, b, c = x

x[0].foo()  # foo
x[1].bar()  # far
x[2].baz()  # baz

a.foo()  # foo
b.bar()  # far
c.baz()  # baz
