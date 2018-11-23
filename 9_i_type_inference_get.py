


class MyField:
    def __get__(self, instance, owner):
        return [1, 2, 3]


class C:
    field1 = MyField()


C().field1.append()  # append