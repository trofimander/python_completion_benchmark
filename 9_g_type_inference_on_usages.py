class A():
    def foo999(self):
        pass


def f(x):
    x.foo999()  # foo


f(A())
