globals()['foo'] = 0
del foo

bar = 1

del bar

print(foo)  # NO foo
print(bar)  # NO bar
