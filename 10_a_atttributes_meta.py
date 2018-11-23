class M(type):
    def foo(cls):
        pass


class C(metaclass=M):
    def bar(self):
        pass

    def __init__(self):
        self.baz = 1


x1 = M.foo  # foo
x2 = C.foo  # foo
x3 = C().foo  # NO!


x4 = C.bar  # bar
x5 = C().bar  # bar

x6 = C.baz  # NO!
x7 = C().baz  # baz

