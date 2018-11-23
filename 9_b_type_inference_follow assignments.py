class C:
    def foo(self):
        pass


class D:
    def bar(self):
        pass

def f(c):
    x = C()
    y = x
    y.foo()  # foo
    if c:
        z = y
    else:
        z = D()
    z.foo()  # foo
    z.bar()  # bar
