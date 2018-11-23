class C:
    pass


def f():
    a = C()
    a.foo = 1
    print(a.foo)  # foo
    return a


b = f()


print(b.foo)  # foo