# Example: imported names in various scopes
# Given that all the modules are importable

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

del foo
foo  # No 'foo' in completion