class A(object):
    class_attr = "attr"

    def __init__(self):
        self.attr = 1

    def foo(self):
        self.attr  # attr

    @classmethod
    def static(cls):
        cls.class_attr # class_attr

A.class_attr # class_attr
A.static() # static
