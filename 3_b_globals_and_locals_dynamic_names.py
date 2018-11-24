globals()['foo'] = 'bar'
print(foo)  # foo

for i in range(10):
    gloabals()[f'foo{i}'] = f'bar{i}'
print(foo1)  # foo1
print(foo2)  # foo2
