class C:
    def foo(self) -> 'C':  # C
        pass


c = C()

c.foo()  # foo
