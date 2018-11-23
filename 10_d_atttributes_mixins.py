class A1:
    def foo(self):
        self.bar()  # bar


class A2:
    def foo(self):
        self.bar()  # bar


class B(A1):
    def bar(self):
        pass


class D:
    def bar(self):
        pass


class AD(A2, D):
    pass
