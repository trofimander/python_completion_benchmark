class A(object):
    class_attr = "attr"

    def __init__(self):
        self.attr = 1

    def foo(self):
        print(self.attr)  # attr

    @classmethod
    def static(cls):
        print(cls.class_attr) # class_attr

print(A.class_attr) # class_attr
A.static() # static
