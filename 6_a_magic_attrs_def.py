class C(str):
    def __bytes__(self): # __bytes__
        pass

    def find(self): # find
        pass


class A(object):
    barbaz = 2


class B(A):
    barbaz = 3 # barbaz


