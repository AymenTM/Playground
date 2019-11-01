

# # SIZEOF

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # from sys import getsizeof

        # i = 0
        # d = {'name': 'John', 'lname': 'Doe'}
        # t = [('name', 'John'), ('lname', 'Doe')]

        # print(getsizeof(i))
        # print(getsizeof(d))
        # print(getsizeof(t))

# # — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —


# PYTHON BUILT-IN FUNCTIONS

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

#         >>> abs(-10)
#         10

#         >>> abs(-19.27364)
#         19.27364

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

#         >>> l = [1, 2, 3, 0, 5]

#         >>> all(l)
#         False

#         >>> l = ['John', 'Matt', '']

#         >>> all(l)
#         False

#         >>> l = ['John', 'Matt', None]

#         >>> all(l)
#         False

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

#         >>> any('a')
#         True

#         >>> any(['James', '', ''])
#         True

#         >>> any([0, 0, 1, 0])
#         True

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> ascii(342)
        # '342'

        # >>> ascii('some string')
        # "'some string'"

        # >>> bytes([104, 101, 108, 108, 111, 15])
        # b'hello\x0f'

        # >>> ascii(abs)
        # '<built-in function abs>'

        # >>> ascii(int)
        # "<class 'int'>"

        # >>> ascii(str.join)
        # "<method 'join' of 'str' objects>"

        # >>> ascii(int.denominator)
        # "<attribute 'denominator' of 'int' objects>"

        # >>> ascii(int(9).denominator)
        # '1'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

#         >>> bool()
#         False

#         >>> bool(0)
#         False

#         >>> bool(1)
#         True

#         >>> bool('')
#         False

#         >>> bool('a')
#         True

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

  #   # playground.py
  # — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 

  #   breakpoint()

  #   greetings = 'Hello'
  #   audience = 'World'

  #   print(f'{greetings}, {audience}!')

  # — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 

  #   ➜  Playground git:(master) ✗ python3 Python/playground.py
  #   > /Users/*/Desktop/Playground/Python/playground.py(4)<module>()
  #   -> greetings = 'Hello'
  #   (Pdb) _

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> mutable_byte_string = bytearray('τoρνoς', encoding='utf-8')

        # >>> mutable_byte_string
        # bytearray(b'\xcf\x84o\xcf\x81\xce\xbdo\xcf\x82')

        # >>> list(mutable_byte_string)
        # [207, 132, 111, 207, 129, 206, 189, 111, 207, 130]

        # >>> mutable_byte_string[3] = 208

        # >>> list(mutable_byte_string)
        # [207, 132, 111, 208, 129, 206, 189, 111, 207, 130]

        # >>> mutable_byte_string
        # bytearray(b'\xcf\x84o\xd0\x81\xce\xbdo\xcf\x82')

        # >>> mutable_byte_string.decode('utf-8')
        # 'τoЁνoς'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> bytes([104, 101, 108, 108, 111])
        # b'hello'

        # >>> bytes('hello', encoding='ASCII')
        # b'hello'

        # >>> bytes('τoρνoς', encoding='utf-8')
        # b'\xcf\x84o\xcf\x81\xce\xbdo\xcf\x82'

        # >>> list(bytes('τoρνoς', encoding='utf-8'))
        # [207, 132, 111, 207, 129, 206, 189, 111, 207, 130]

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

#         >>> callable(int)
#         True

#         >>> int.__call__()
#         0

#         >>> int()
#         0

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

#         >>> chr(97)
#         'a'

#         >>> chr(8364)
#         '€'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

#         >>> abs(-10)
#         10

#         >>> abs(-19.27364)
#         19.27364

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

#         >>> l = [1, 2, 3, 0, 5]

#         >>> all(l)
#         False

#         >>> l = ['John', 'Matt', '']

#         >>> all(l)
#         False

#         >>> l = ['John', 'Matt', None]

#         >>> all(l)
#         False

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

#         >>> any('a')
#         True

#         >>> any(['James', '', ''])
#         True

#         >>> any([0, 0, 1, 0])
#         True

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

#         >>> bool()
#         False

#         >>> bool(0)
#         False

#         >>> bool(1)
#         True

#         >>> bool('')
#         False

#         >>> bool('a')
#         True

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

#         class C:
#             @classmethod
#             def func(cls, *args):
# #              ...

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # class C:
        #     letter = 'c'

        # delattr(instance, 'letter')

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

    #     >>> d = dict([('name', 'James'), ('age', 12)])

    #     >>> d
    #     {'name': 'James', 'age': 12}


    #     >>> d = dict({'name': 'James', 'age': 12})

    #     >>> d
    #     {'name': 'James', 'age': 12}


    #     >>> d = dict(name='James', age=12)

    #     >>> d
    #     {'name': 'James', 'age': 12}


    #     >>> d = dict()

    #     >>> d
    #     {}

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

    #     # Brand New Python Interative Shell

    #     >>> dir()
    #     ['__annotations__', '__builtins__', '__doc__', '__loader__',
    #      '__name__', '__package__', '__spec__']

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

    #     >>> class C:
    #     ...     """
    #     ...     Autobiographical class for the letter 'C'.
    #     ...     """
    #     ...
    #     ...     letter = 'c'
    #     ...
    #     ...     def print_me():
    #     ...         print('c')
    #     ...

    #     >>> dir(C)
    #     ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
    #     '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__',
    #     '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
    #     '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
    #     'letter', 'print_me']

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

    #     >>> dir(dict)
    #     ['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__',
    #     '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__',
    #     '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__',
    #     '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
    #     '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__',
    #     'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem',
    #     'setdefault', 'update', 'values']

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

#         >>> import sys

#         >>> dir(sys)
#         ['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__',
#         '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__',
#         '__stderr__', '__stdin__', '__stdout__', '_clear_type_cache', '_current_frames',
#         '_debugmallocstats', '_framework', '_getframe', '_git', '_home', '_xoptions',
#         'abiflags', 'api_version', 'argv', 'base_exec_prefix', 'base_prefix', 'breakpointhook',
#         'builtin_module_names', 'byteorder', 'call_tracing', 'callstats', 'copyright',
#         'displayhook', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix',
#         'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks',
#         'get_coroutine_origin_tracking_depth', 'get_coroutine_wrapper', 'getallocatedblocks',
#         'getcheckinterval', 'getdefaultencoding', 'getdlopenflags',
#         'getfilesystemencodeerrors',
#         ...

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

#         >>> d = divmod(342, 5)

#         >>> d
#         (68, 2)

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

#         >>> q, r = divmod(8712, 9)

#         >>> q
#         968

#         >>> r
#         0

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # # playground.py
        # print('Hello World!')

        # exec(
        #     compile(
        #             source=open('playground.py').read(),
        #             filename='errors.log',
        #             mode='exec'
        #     )
        # )

        # # Output:
        # Hello World!

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # exec("""

        # for i in range(5):
        #     print('This function is cool!')

        # print('\\nOk we are done!')

        #     """)

        # Output:
        # This function is cool!
        # This function is cool!
        # This function is cool!
        # This function is cool!
        # This function is cool!

        # Ok we are done!

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> code_obj = compile(
        #                         source=open('playground.py').read(),
        #                         filename='error.log',
        #                         mode='exec'
        #                 )

        # >>> code_obj
        # <code object <module> at 0x1090b1f60, file "error.log", line 245>

        # >>> exec(code_obj)
        # Hello World!

        # >>> eval(code_obj)
        # Hello World!

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> list(
        # ...     filter(
        # ...             lambda x: x % 2 is 0,
        # ...             range(1, 11)
        # ...     )
        # ... )
        # [2, 4, 6, 8, 10]

        # >>> list(itertools.filterfalse(lambda x: x % 2 is 0, range(1, 11)))
        # [1, 3, 5, 7, 9]

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # # Money
        # rich & poor dad
        # 4-hour work week

        # # Emotional, Social Skill
        # 48 Laws of Power
        # How to Win Friends and Influence People

        # # Man
        # The Way of the Superior Man
        # Man in Search of meaning - victor frankl
        # Mastery by george lenard

        # # Mind and Stoicism
        # Mindfullness for Beginners: Reclaiming the Present Moment and your Life - John Cabedsen
        # Enchiridion - Epictetus
        # The Obstacle is the Way - Ryan Holiday

        # Recommended Authors:
        # Epictetus
        # Cenyca
        # Marcus Aurelius

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> class C:
        # ...     letter = 'c'
        # ...

        # >>> getattr(C, 'letter')
        # 'c'

        # >>> C.letter
        # 'c'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> globals()
        # {'__name__': '__main__', '__doc__': None, '__package__': None,
        # '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
        # '__spec__': None, '__annotations__': {},
        # '__builtins__': <module 'builtins' (built-in)>}

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> class C:
        # ...     letter = 'c'
        # ...

        # >>> hasattr(C, 'letter')
        # True

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> hash('2019')
        # 8381135195210278961

        # >>> hash('hey John')
        # 32976569263748556

        # >>> hash(23)
        # 23

        # >>> hash(9347)
        # 9347

        # >>> hash(-298437)
        # -298437

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> help('itertools.tee')


        # Help on built-in function tee in itertools:

        # itertools.tee = tee(...)
        #     tee(iterable, n=2) --> tuple of n independent iterators.
        # (END)

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> def say_hi():
        # ...     """Prints 'hi' to screen."""
        # ...     print('hi')

        # >>> help(say_hi)


        # Help on function say_hi in module __main__:

        # say_hi()
            # Prints 'hi' to screen.

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> help(list)

        # >>> help(bool)

        # >>> help(zip)

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —


#         >>> a = 1
#         >>> b = 0

#         >>> id(a)
#         4346801232

#         >>> id(b)
#         4346801200


#         >>> x = y = 3

#         >>> id(x)
#         4346801296

#         >>> id(y)
#         4346801296


#         >>> c = 1
#         >>> d = 0
#         >>> e = 3

#         >>> id(c)
#         4346801232

#         >>> id(d)
#         4346801200

#         >>> id(e)
#         4346801296


#         >>> L1 = [1, 2, 3, 4]
#         >>> L2 = [1, 2, 3, 4]

#         >>> id(L1)
#         4349136136

#         >>> id(L2)
#         4349136840


# # — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

#         >>> input('Name: ')
#         Name: _

#         >>> input('Name: ')
#         Name: Jim
#         'Jim'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> int(10)
        # 10

        # >>> int('125')
        # 125

        # >>> int('5A', base=16)
        # 90

        # >>> int('101', base=2)
        # 5

        # >>> int('17777777777', base=8)
        # 2147483647

        # >>> int('7fffffff', base=16)
        # 2147483647

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> class C:
        # ...     letter = 'c'
        # ...

        # >>> inst = C()

        # >>> inst
        # <__main__.C object at 0x10373fb70>

        # >>> isinstance(inst, C)
        # True

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> class Letter(object):
        # ...     pass
        # ...

        # >>> class C(Letter):
        # ...     letter = 'c'
        # ...

        # >>> issubclass(C, Letter)
        # True

        # >>> issubclass(C, C)
        # True

        # >>> issubclass(C, object)
        # True

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # a = (x for x in range(1, 4))    # generator
        # b = [1, 2, 3]                   # list

        # # print(iter(a) is iter(a)) # —> True   # iterator (exhaustable only once)
        # # print(iter(b) is iter(b)) # —> False  # list (exhaustable multiple times)

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # from itertools import tee

        # class Reiterable(object):

        #     def __init__(self, iterator):
        #         self.iterator = iterator

        #     def __iter__(self):
        #         self.iterator, copy = tee(self.iterator)
        #         return copy

        # a = Reiterable(iter([1, 2, 3]))

        # print(f'Sum: {sum(a)}')
        # print('Values:')
        # for i in a:
        #     print(i)

        # Sum: 6
        # Values:
        # 1
        # 2
        # 3

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # from contextlib import contextmanager
        # from sys import getsizeof

        # @contextmanager
        # def timer():
        #     """
        #     Times the execution time of the entire with statement block
        #     and logs it after its excution.
        #     """

        #     from time import perf_counter

        #     try:
        #         t1 = perf_counter()
        #         yield
        #     except Exception:
        #         pass
        #     finally:
        #         t2 = perf_counter()
        #         print(f"[Finished block in {t2 - t1:.9f}s]")

        # a = [x for x in range(1, 10000000)]
        # b = (x for x in range(1, 10000000))
        # c = iter(a)
        # d = range(1, 10000000)

        # print(getsizeof(a))
        # print(getsizeof(b))
        # print(getsizeof(c))
        # print(getsizeof(d))

        # with timer():
        #     for i in a:
        #         pass
        # with timer():
        #     for i in b:
        #         pass
        # with timer():
        #     for i in c:
        #         pass
        # with timer():
        #     for i in d:
        #         pass


# 10 Million Intergers
# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 
# | Type      |  Syntax                           |  Size            |  Speed to Iterate Through          |
# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 
# | List      |  [x for x in range(1, 10000000)]  |  81528056 bytes  |  [Finished block in 0.621161122s]  |
# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 
# | Generator |  (x for x in range(1, 10000000))  |  120  bytes      |  [Finished block in 1.661366191s]  |
# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 
# | Iterator  |  iter(List)                       |  56   bytes      |  [Finished block in 0.581645339s]  |
# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 
# | Range     |  range(1, 10000000)               |  48   bytes      |  [Finished block in 0.931747395s]  |
# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 

# 100 Intergers
# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 
# | Type      |  Syntax                           |  Size            |  Speed to Iterate Through          |
# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 
# | List      |  [x for x in range(1, 100)]       |  912 bytes       |  [Finished block in 0.000011855s]  |
# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 
# | Generator |  (x for x in range(1, 100))       |  120  bytes      |  [Finished block in 0.000015490s]  |
# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 
# | Iterator  |  iter(List)                       |  56   bytes      |  [Finished block in 0.000006913s]  |
# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 
# | Range     |  range(1, 100)                    |  48   bytes      |  [Finished block in 0.000008412s]  |
# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> a = [1, 2, 3]
        # >>> b = iter(a)

        # >>> a
        # [1, 2, 3]

        # >>> b
        # <list_iterator object at 0x10a69bb70>

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> a = [1, 2, 3, 4, 5]

        # >>> len(a)
        # 5

        # >>> b = ['John', 'Tom', 'Ben', 'Marc']

        # >>> len(b)
        # 4

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # # List
        # >>> a = list([1, 2, 3, 4, 5])

        # >>> a
        # [1, 2, 3, 4, 5]


        # # Set
        # >>> b = list({'John', 'Tom', 'Ben', 'Marc'})

        # >>> b
        # ['Marc', 'Ben', 'Tom', 'John']


        # # List of Tuples
        # >>> c = list([('name', 'Jack'), ('age', 23)])

        # >>> c
        # [('name', 'Jack'), ('age', 23)]


        # # Dict
        # >>> d = list({'name': 'Jack', 'age': 23})

        # >>> d
        # ['name', 'age']

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> locals()
        # {'__name__': '__main__', '__doc__': None, '__package__': None,
        # '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
        # '__spec__': None, '__annotations__': {},
        # '__builtins__': <module 'builtins' (built-in)>}

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> m = map(lambda x: x + 1, [1, 2, 3])

        # >>> m
        # <map object at 0x10a751c18>

        # >>> list(m)
        # [2, 3, 4]


        # >>> list(map(lambda x, y: x + y, [1, 2, 3], [1, 2, 3]))
        # [2, 4, 6]


        # >>> list(
        # ...     map(
        # ...         lambda x, y, z: x + y + z,
        # ...         [1, 2, 3], [1, 2, 3], [1, 2, 3]
        # ...     )
        # ... )
        # [3, 6, 9]

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —


        # >>> tuple(map(lambda x: x + 1, [1, 2, 3]))
        # (2, 3, 4)

        # >>> set(map(lambda x: x + 1, [1, 2, 3]))
        # {2, 3, 4}

        # >>> dict(map(lambda x: x + 1, [1, 2, 3]))
        # ...
        # TypeError: cannot convert [...]


# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> from itertools import starmap

        # >>> myTuple = [(1, 1), (2, 2), (3, 3)]

        # >>> starmap(lambda x, y: x + y, myTuple)
        # <itertools.starmap object at 0x10aa36b00>

        # >>> list(starmap(lambda x, y: x + y, myTuple))
        # [2, 4, 6]


        # >>> myTuple = [(1, 2), (2, 3), (3, 4)]

        # >>> list(starmap(lambda x, y: x + y, myTuple))
        # [3, 5, 7]


        # >>> myTuple = [(1, 2, 3), (2, 3, 4), (3, 4, 5)]

        # >>> list(starmap(lambda x, y, z: x + y + z, myTuple))
        # [6, 9, 12]

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> max([], default='Empty')
        # 'Empty'

        # >>> max([1, 2, 3, 4, 5], default='Empty')
        # 5

        # >>> max(
        # ...     [('John', 13), ('Felix', 16), ('James', 15)],
        # ...     key=lambda item: item[1],
        # ...     default='Empty'
        # ... )
        # ('Felix', 16)

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> max([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15])
        # [11, 12, 13, 14, 15]

        # >>> max(
        # ...     [1, 2, 3, 4, 5], [0, 7, 8, 9, 10], [-1, 12, 13, 14, 15],
        # ...     key=lambda item: item[0]
        # ... )
        # [1, 2, 3, 4, 5]

        # >>> max(
        # ...     [1, 2, 3, 4, 5], [20, 7, 8, 9, 10], [-100, 12, 13, 14, 15],
        # ...     key=sum
        # ... )
        # [20, 7, 8, 9, 10]

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> a = iter([1, 2, 3, 4, 5])

        # >>> next(a)
        # 1
        # >>> next(a)
        # 2
        # >>> next(a)
        # 3
        # >>> next(a)
        # 4
        # >>> next(a)
        # 5
        # >>> next(a, 'Empty')
        # 'Empty'
        # >>> next(a, 'Empty')
        # 'Empty'

        # ...

        # >>> next(a)
        # Traceback (most recent call last):
        #   File "<stdin>", line 1, in <module>
        # StopIteration

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # Help on class object in module builtins:

        # class object
        #  |  The most base type
        #  ESC

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —


        # >>> class Alphabet(object):
        # ...     pass
        # ...

        # >>> class C(Alphabet):
        # ...     pass
        # ...


# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> ord('a')
        # 97

        # >>> ord('€')
        # 8364

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> pow(10, 2)
        # 100

        # >>> pow(-10, 3)
        # -1000

        # >>> pow(10, -2)
        # 0.01

        # >>> pow(3, 3, 5)
        # 2

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —


        # >>> print('Hello, world!', end='~\n')
        # Hello, world!~

        # >>> print('Ok im done.', end='~\n')
        # Ok im done.~


        # >>> names = ['John', 'Mark', 'Steve']

        # >>> print(*names, sep=' ; ')
        # John ; Mark ; Steve


        # >>> name = 'Tom'
        # >>> list = [1, 2, 3]
        # >>> years = (2012, 2013, 2015, {2019, 2019})

        # >>> print('hello', 32, name, list, years, sep='  ;  ')
        # hello  ;  32  ;  Tom  ;  [1, 2, 3]  ;  (2012, 2013, 2015, {2019})


        # >>> with open('file.txt', 'wt') as f:
        # ...     print('Hello world!', file=f)
        # ...

        # # file.txt
        # Hello world!

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> range(10)
        # range(0, 10)

        # >>> list(range(10))
        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        # >>> tuple(range(100, 151, 10))
        # (100, 110, 120, 130, 140, 150)

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> a = [1, 2, 3]

        # >>> repr(a)
        # '[1, 2, 3]'


        # >>> d = {'name': 'John', 'age': 23}

        # >>> repr(d)
        # "{'name': 'John', 'age': 23}"


        # >>> fd = open('playground.js')

        # >>> repr(fd)
        # "<_io.TextIOWrapper name='playground.js' mode='r' encoding='UTF-8'>"

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> class Letter(object):
        # ...
        # ... def __init__(self, letter):
        # ...     self.letter = letter
        # ...
        # ... def __repr__(self):
        # ...     return f'Letter({self.letter})'

        # >>> c = Letter('c')

        # >>> repr(c)
        # "Letter('c')"

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> a = [1, 2, 3]
        # >>> b = reversed(a)

        # >>> b
        # <list_reverseiterator object at 0x10377c048>

        # >>> list(b)
        # [3, 2, 1]

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> my_name = 'Tonny Blurigo'
        # >>> rev_my_name = reversed(my_name)

        # >>> ''.join(rev_my_name)
        # 'ogirulB ynnoT'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> names = ('Philip', 'Mark', 'John')
        # >>> rev_names = reversed(names)

        # >>> tuple(rev_names)
        # ('John', 'Mark', 'Philip')

        # >>> tuple(rev_names)
        # ()

        # empty because we already iterated
        # over the iterator once, thus exhausting
        # it

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> d = {'name': 'Gabriel', 'age': 23}

        # >>> rev_d = reversed(d)
        # ...
        # TypeError: 'dict' object is not reversible

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> years = {2018, 2019, 2020}

        # >>> rev_years = reversed(years)
        # ...
        # TypeError: 'set' object is not reversible

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> round(7.92372634)
        # 8

        # >>> round(7.42372634)
        # 7

        # >>> round(2.34827342, 3)
        # 2.348

        # >>> round(2.34827342, 4)
        # 2.3483

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> a = set([1, 1, 1, 2, 2, 3, 4, 5, 5, 5, 6, 7])

        # >>> a
        # {1, 2, 3, 4, 5, 6, 7}


        # >>> names = set(['John', 'James', 'John', 'Mark'])

        # >>> names
        # {'John', 'Mark', 'James'}

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> class Letter(object):
        # ...
        # ...     def __init__(self, letter):
        # ...             self.letter = letter
        # ...
        # >>> c = Letter('c')

        # >>> c.letter = 'z'

        # >>> setattr(c, 'letter', 'z')

        # >>> c.letter
        # 'z'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> nums = [1, 2, 3, 4, 5]

        # >>> nums[:-1]
        # [1, 2, 3, 4]

        # >>> nums[0:3]
        # [1, 2, 3]

        # >>> nums[0:-1:2]
        # [1, 3]

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —


      #   >>> names = ['Tom', 'Bob', 'Sam', 'Alex', 'Jim']


      #   REGULAR SLICING
      # —————————————————————————————————————————

      #   >>> names[0:3]
      #   ['Tom', 'Bob', 'Sam']


      #   SLICE()
      # —————————————————————————————————————————

      #   >>> frozen_slicer = slice(0, 3)

      #   >>> names[frozen_slicer]
      #   ['Tom', 'Bob', 'Sam']


      #   iSLICE()
      # —————————————————————————————————————————

      #   >>> islice(names, 0, 3)
      #   <itertools.islice object at 0x1099c0278>

      #   >>> list(islice(names, 0, 3))
      #   ['Tom', 'Bob', 'Sam']


# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> with open('file.txt', 'rt') as f:
        # ...
        # ...     desired_lines = islice(f, 0, 3)
        # ...     for line in desired_lines:
        # ...             print(line, end='')
        # ...
        # Line 1
        # Line 2
        # Line 3

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> from itertools import islice


        # >>> names = ['Dave', 'Bob', 'Sam', 'Tom']

        # >>> s = islice(names, 0, 3)

        # >>> s
        # <itertools.islice object at 0x103a9e4f8>

        # >>> list(s)
        # ['Dave', 'Bob', 'Sam']

        # >>> for name in s:
        # ...     print(name)
        # ...
        # Dave
        # Bob
        # Samz

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> nums = [9, 3, 5, 8, 2, 7, 0, 4, 1, 6]

        # >>> sorted(nums)
        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        # >>> sorted(nums, reverse=True)
        # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> names = ['Stacy', 'John', 'Abby', 'Marc', 'Ben']

        # >>> sorted(names, key=lambda name: name[0])
        # ['Abby', 'Ben', 'John', 'Marc', 'Stacy']

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> str(28347)
        # '28347'

        # >>> str('Jack')
        # 'Jack'

        # >>> str(['John', 'Mike', 'Steve'])
        # "['John', 'Mike', 'Steve']"

        # >>> str(dict(name='John', age=23))
        # "{'name': 'John', 'age': 23}"

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> str(abs)
        # '<built-in function abs>'

        # >>> str(int)
        # "<class 'int'>"

        # >>> str(str.join)
        # "<method 'join' of 'str' objects>"

        # >>> str(int.denominator)
        # "<attribute 'denominator' of 'int' objects>"

        # >>> str(int(9).denominator)
        # '1'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> str(b'\xcf\x84o\xcf\x81\xce\xbdo\xcf\x82', encoding='utf-8', errors='strict')
        # 'τoρνoς'

        # >>> str(b'\xcf\x84o\xcf\x81\xce\xbdo\xcf\x82', encoding='utf-16', errors='strict')
        # '蓏콯캁澽苏'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> 'τoρνoς'.encode('utf-8')
        # b'\xcf\x84o\xcf\x81\xce\xbdo\xcf\x82'

        # >>> b'\xcf\x84o\xcf\x81\xce\xbdo\xcf\x82'.decode('utf-8')
        # 'τoρνoς'

        # >>> '蓏콯캁澽苏'.encode('utf-16')
        # b'\xff\xfe\xcf\x84o\xcf\x81\xce\xbdo\xcf\x82'

        # >>> b'\xff\xfe\xcf\x84o\xcf\x81\xce\xbdo\xcf\x82'.decode('utf-16')
        # '蓏콯캁澽苏'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        # 55

        # >>> sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
        # 60


        # i.e —> We start at 5 and add to it the sum of the iterable
        # 5 + 55 = 60


        # >>> sum([1.5, 2.5, 3.5])
        # 7.5

        # >>> sum([-1.5, -2.5, -3.5])
        # -7.5

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # Example 1:


        # class English(object):

        #     def print_lang(self):
        #         print('I am the English language.')


        # class Letter(English):

        #     letter_type = 'ASCII Letters'

        #     def print_alphabet(self):
        #         print('abcdefghijklmnopqrstuvwxyz')

        #     def print_numbers(self):
        #         print('0123456789')


        # class C(Letter):

        #     def method(self):

        #         LetterClass, EnglishClass = super(), super()

        #         print(LetterClass)
        #         print(EnglishClass)

        #         EnglishClass.print_lang()

        #         LetterClass.print_alphabet()
        #         LetterClass.print_numbers()
        #         print(LetterClass.letter_type)


        # C().method()


        # <super: <class 'C'>, <C object>>
        # <super: <class 'C'>, <C object>>
        # I am the English language.
        # abcdefghijklmnopqrstuvwxyz
        # 0123456789
        # ASCII Letters

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # class Employee(object):

        #     def __init__(self, first, last, *, salary):

        #         self.first = first
        #         self.last = last
        #         self.salary = salary

        #     def __str__(self):
        #         return (f'{self.first} {self.last} - ${self.salary}/yr')

        # class Developper(Employee):

        #     def __init__(self, first, last, prog_lang, *, salary):

        #         super().__init__(first, last, salary=salary)
        #         self.prog_lang = prog_lang

        #         print(super().__init__) # for demonstration purposes


        # emp_1 = Employee('John', 'Herbert', salary=55000)
        # dev_1 = Developper('Sam', 'Carter', 'Python', salary=75000)

        # print(emp_1)
        # print(dev_1)

        # <bound method Employee.__init__ of <__main__.Developper object at 0x10811f7f0>>
        # John Herbert - $55000/yr
        # Sam Carter - $75000/yr

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> tuple(['James', 'Gordon', 'Tom'])
        # ('James', 'Gordon', 'Tom')

        # >>> tuple([1, 2, 3, 4, 5])
        # (1, 2, 3, 4, 5)

        # >>> tuple([{'name': 'James', 'age':23}, {'name': 'Tom', 'age': 12}])
        # ({'name': 'James', 'age': 23}, {'name': 'Tom', 'age': 12})

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> class C(object):
        # ...
        # ...     letter = 'c'
        # ...

        # >>> C
        # <class '__main__.C'>

        # >>> type('C', (object, ), dict(letter='c'))
        # <class '__main__.C'>

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> class Letter(object):
        # ...
        # ...     def __init__(self, letter):
        # ...             self.letter = letter
        # ...

        # >>> c = Letter('c')

        # >>> vars(c)
        # {'letter': 'c'}

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> class Letter(object):
        # ...
        # ...     def __init__(self, letter):
        # ...             self.letter = letter
        # ...

        # >>> c = Letter('c')

        # >>> vars(c)
        # {'letter': 'c'}

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

        # >>> x = [1, 2, 3]
        # >>> y = [4, 5, 6]

        # >>> zip(x, y)
        # <zip object at 0x10a795248>

        # >>> list(zip(x, y))
        # [(1, 4), (2, 5), (3, 6)]

        # >>> list(zip(*zip(x, y)))
        # [(1, 2, 3), (4, 5, 6)]

        # >>> x2, y2, = zip(*zip(x, y))

        # >>> list(x2)
        # [1, 2, 3]

        # >>> list(y2)
        # [4, 5, 6]

        # >>> x == list(x2) and y == list(y2)
        # True

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —
