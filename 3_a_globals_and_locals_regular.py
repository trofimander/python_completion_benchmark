import foo

foo  # foo


def f():
    import bar
    bar  # bar


class C:
    import baz
    baz  # baz


bar  # No 'bar' in completion
baz  # No 'baz' in completion