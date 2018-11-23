# Code completion categories

1. Keywords
    * [x] Shown only where it is syntactically appropriate (mostly covered in PyCharm)
      
          await # No 'await' in completion
          
          async def foo(x):  # async, def
              await x  # await
              await def  # No 'def' in completion
    
2. Built-in names
    * [x] Standard builtins
    
          print(len('foo'))  # print, len
    
    * [x] Built-ins dynamically added to `builtins` in this or another module (not in PyCharm)
    
          import builtins
          buitlins.foo = 'bar'
          
          foo  # foo
          bar  # No 'bar' in completion
    
3. Globals and locals
    * [x] Regular static names with respect to scopes
        * Names: imports, functions, classes, assignments, parameters. Scopes: module, class, function, comprehension, lambda
        
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
        
        * Names can become unavailable after `del` (not in PyCharm)
    * [x] Per-module dynamic names via modification of `globals()` and `locals()` (not in PyCharm)
    
          globals()['foo'] = 'bar'
          print(foo)  # foo
          
          for i in range(10):
              gloabals()[f'foo{i}'] = f'bar{i}'
          print(foo1)  # foo1
          print(foo2)  # foo2

          # and so on, depending on how powerful the static evaluator is

4. Import statements
    * [x] Regular Python packages and modules that exist on the file system in analyzed directories
        
          import math  #  math
        
    * [x] Python 3 namespace packages (without `__init__.py`)
    
          # Given this `sys.path` root structure:
          #
          # syspath_root1/
          #   nspkg1/
          #     m1.py
          # syspath_root2/
          #   nspkg1/
          #     m2.py
          
          import nspkg1  # nspkg1
          import nspkg1.m1  # m1
          import nspkg1.m2  # m2
    
    * [x] Module and package attributes in `from`-imports
    
          # Given that package1/__init__.py has 'foo' in it
          from package1 import foo  # foo
          
          # Given that module1.py has `bar` in it
          from module1 import bar  # bar
    
    * [x] Names available for star-imports (limited by `__all__`)
    * [ ] Setuptools namespace packages (e.g. still in use for `zope.interface` where `zope` is a namespace package)
    * [ ] Dynamic modification of `sys.path` in user or library code (not in PyCharm)
    * [ ] Import hooks via `sys.meta_path` and `sys.path_hooks` (not in PyCharm)
    
5. Keyword arguments
    * [x] Static keyword arguments

          def f(*, foo, bar): ...
      
          f(foo=1, bar=2)  # foo, bar
    
    * [ ] Library-specific dynamic keyword arguments (e.g. `filter()` arguments in Django ORM, where `def filter
    (**kwargs): ...`)

6. Overridden and magic attributes
    * [x] Functions in classes after `def`
    * [x] Class-level assignments
7. Special strings
    * [x] Key names for dicts and dict-like objects (only for locally-defined non-nested dicts in PyCharm)
    * [x] Names for `__all__` in modules
    * [x] File system paths in string literals (only in some places in PyCharm)
    * [ ] Library-specific strings (e.g. foreign keys in Django ORM or various settings in settings.py)
8. Type hints
    * [x] Python stubs (*.pyi) take precedence over regular (*.py) files in resolving all names
    * [x] String-based type hints
    
          class C:
              def f(self) -> 'C':   # C
                  pass
     
    * [x] Comment-based type hints
    
          def f(x):
              # type: (int) -> str
              # 'int', 'str' in the line above

9. Type inference
        * [x] Simple constructor calls / literals
        
              x = [1, 2, 3]  # x is a List[int]
              
              class C: ...
              y = C()  # y is a C
        
        * [x] Follow assignments chain in a single scope
        
              def f(c):
                  x = [1, 2, 3]
                  y = x  # y is a List[int]
                  if c:
                      z = y
                  else:
                      z = 'foo'
                  print(z)  # z is a Union[List[int], str]
        
        * [x] Return types of function calls, call trees (can span many modules)
        
              # Assuming h() returns an int
              from module1 import h
        
              def f():
                  return 0
              
              def g():
                  return f(), 'foo', h()
              
              x = g()  # x is a Tuple[int, str, int]
              
        * [x] Instance checks (`isinstance`, `issubclass`)
        
        * [x] Type hints
        
              def f(x: int) -> int: ...
                  x  # x is an int
              
              y = f()  # y is an int
        
        * [x] Types for `self` / `cls` parameters in methods
        
        * [x] Types of parameters based on their usages (only for module-local usages in PyCharm)
        
              def f(x):
                  x  # x is a str (only for code completion in PyCharm)
                  
              f('foo')
        
        * [x] Dynamic imports via `__import__` (not in PyCharm)
        
              sys = __import__('sys')  # 'sys' can be an arbitrary complex expression, depending on how powerful the static evaluator is
              sys  # <Module 'sys'> with all its attributes
              
        * [x] Types provided via the descriptor protocol (`__get__`)
        
        * [x] Type for the components of a tuple
        
              x = (1, 'foo', [1, 2, 3])
              a, b, c = x  # a is an int, b is a str, c is a List[int]
              x[0]  # x[0] is an int
              x[1]  # x[1] is a str
              x[2]  # x[s] is a List[int]
        
10. The attributes of an object
    * [x] Static attributes of an object (provided that we know its type, see the section about types above)
        * Class + instance attributes for an instance
        * Metaclass + class attributes for a class
        * [ ] Compliance to Python MRO attribute resolution order for inheritance hierarchies
    * [x] Instance attributes added after an object has been created (only for local definition scopes in PyCharm)
    * [x] Class attributes added after a class has been created (only for local definition scopes in PyCharm)
    * [x] Attributes of descendant classes available in a mixin class (not in PyCharm)
    * [x] Dynamic attributes via `__getattr__` and `__getattribute__`, depending on how powerful the static evaluator is
     (not in PyCharm)
    * [x] Dynamic attributes after `hasattr()` checks
    * [x] Highly dynamic stdlib classes and their descendants (namedtuples and dataclasses in PyCharm)
    * [x] Attributes of binary modules (available via skeletons in PyCharm)
    * [ ] Dynamic attributes via custom class creation logic in metaclasses (not in PyCharm)
    