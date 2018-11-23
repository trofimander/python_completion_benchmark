class A:
    def foo(self):
        pass


def f(x: A) -> A:
    x.foo()  # foo
    return A()


y = f(A())  # y is A
y.foo()  # foo
