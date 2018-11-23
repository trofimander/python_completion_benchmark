class A:
    def __getattr__(self, item):
        if item == 'foo':
            return item


x = A()
x.foo  # foo


class B:
    def __getattr__(self, item):
        for i in range(1, 10):
            if item == "foo" + str(i):
                return item


b = B()

b.foo1  # foo1


class C:
    pass

c = C()

for i in range(1, 10):
    setattr(c, "foo" + str(i), 1)


c.foo1 # foo1


for i in range(1, 10):
    setattr(C, "foo" + str(i), 1)

C.foo1 # foo1