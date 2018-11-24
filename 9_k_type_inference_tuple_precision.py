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

x[0].bar()  # NO bar
x[1].baz()  # NO baz
x[2].foo()  # baz

a.bar()  # NO bar
b.baz()  # NO baz
c.foo()  # NO foo
