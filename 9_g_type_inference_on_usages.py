class A():
    def foo(self):
        pass


def f(x):
    x.foo()  # foo


f(A())
