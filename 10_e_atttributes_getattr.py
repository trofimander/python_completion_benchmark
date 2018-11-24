class A:
    def __getattr__(self, item):
        if item == 'foogza':
            return item


x = A()
x.foogza  # foogza


class B:
    def __getattr__(self, item):
        for i in range(1, 10):
            if item == "foogza" + str(i):
                return item


b = B()

b.foogza1  # foogza1


class C:
    pass

c = C()

for i in range(1, 10):
    setattr(c, "foorma" + str(i), 1)


c.foorma2 # foorma1


for i in range(1, 10):
    setattr(C, "foo" + str(i), 1)

C.foo1 # foo1
