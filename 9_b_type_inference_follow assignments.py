def f(c):
    x = [1, 2, 3]
    y = x  # y is a List[int]
    y.append()  # append
    if c:
        z = y
    else:
        z = 'foo'
    z.append()  # append
    z.find()  # find
    print(z)  # z is a Union[List[int], str]
