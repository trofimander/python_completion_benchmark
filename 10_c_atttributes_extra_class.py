class C:
    pass


C.foo = 1
print(C.foo)  # foo

from module1 import E

E.bar = 1

print(E.bar)  # bar

print(E.foobar)  # foobar
