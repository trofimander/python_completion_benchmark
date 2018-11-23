class A:
    def foo(self):
        pass


def foo(x):
    if isinstance(x, A):
        x.foo()  # foo
