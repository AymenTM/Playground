#!/usr/local/bin/python3.7

# Testing more Advanced Ctype Module Features

from ctypes import *

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		# >>> ptr = pointer(name)

		# >>> ptr._type_
		# <class 'ctypes.c_wchar_p'>

		# >>> ptr.contents
		# c_wchar_p(4440854416)

		# >>> ptr.contents.value
		# 'John Jones'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		# >>> pi = c_float(3.14)

		# >>> pi
		# c_float(3.140000104904175)

		# >>> pi.value
		# 3.140000104904175

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		# >>> pi = c_double(3.14)

		# >>> pi
		# c_double(3.14)

		# >>> pi.value
		# 3.14

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		# >>> first_character_of_my_name = c_char(b'A')

		# >>> first_character_of_my_name
		# c_char(b'A')

		# >>> first_character_of_my_name.value
		# b'A'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		# >>> first_character_of_my_name = c_wchar('A')

		# >>> first_character_of_my_name
		# c_wchar('A')

		# >>> first_character_of_my_name.value
		# 'A'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		# >>> name = c_char_p(b'John Jones')

		# >>> name
		# c_char_p(4406926512)

		# >>> name.value
		# b'John Jones'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		# >>> name = c_wchar_p('John Jones')

		# >>> name
		# c_wchar_p(4408332432)

		# >>> name.value
		# 'John Jones'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		# >>> name = create_string_buffer(b'John Jones')

		# >>> name
		# <ctypes.c_char_Array_11 object at 0x106ae5510>

		# >>> name.value
		# b'John Jones'

		# >>> name.raw
		# b'John Jones\x00'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		# >>> name = create_string_buffer(b'John Jones', 20)

		# >>> name
		# <ctypes.c_char_Array_20 object at 0x106b12730>

		# >>> name.value
		# b'John Jones'

		# >>> name.raw
		# b'John Jones\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		# >>> lib.function.argtypes = [c_char_p, c_char_p, c_int, c_double]

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		# >>> div = c_int()
		# >>> mod = c_int()

		# >>> ft_divmod(a, b, byref(div), byref(mod))

		# >>> print(f'{div} <==> {div.value}')
		# c_int(20) <==> 20

		# >>> print(f'{mod} <==> {mod.value}')
		# c_int(0) <==> 0

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		# >>> age = c_int(23)
		# >>> ptr = pointer(age)


		# >>> ptr
		# <__main__.LP_c_int object at 0x10ded4400>

		# >>> ptr._type_
		# <class 'ctypes.c_int'>

		# >>> ptr.contents
		# c_int(23)

		# >>> ptr.contents.value
		# 23

		# >>> ptr.contents._type_
		# 'i'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		# >>> class Student(Structure):
		# ...
		# ...     _fields_ = [('name', c_wchar_p),
		# ...                 ('age', c_int),
		# ...                 ('level', c_int)]
		# ...

		# >>> student_1 = Student('james', 15, 10)

		# >>> student_1
		# <__main__.Student object at 0x10621b378>

		# >>> student_1.name
		# 'james'

		# >>> student_1.age
		# 15

		# >>> student_1.level
		# 10

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		# >>> Student_Array = c_wchar_p * 10

		# >>> Grade_2_students = Student_Array( 'James',
		# 									  'Philip',
		# 									  'Tim',
		# 									  'Albert',
		# 									  'Seth',
		# 									  'Sam' )

		# >>> for student in Grade_2_students:
		# ...     print(student)
		# ...
		# James
		# Philip
		# Tim
		# Albert
		# Seth
		# Sam
		# None # i.e it's NULL Pointer
		# None
		# None
		# None

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		# >>> name = create_string_buffer(5)

		# >>> name.raw
		# b'\x00\x00\x00\x00\x00'

		# >>> resize(name, 10)

		# >>> name.raw
		# b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		# >>> name = create_string_buffer(b'James', 10)

		# >>> name.raw
		# b'James\x00\x00\x00\x00\x00'

		# >>> memset(name, 0, len(name.raw))
		# 4459271520

		# >>> name.raw
		# b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

		# >>> memset(name, ord('z'), len(name.raw))
		# 4459271520

		# >>> name.raw
		# b'zzzzzzzzzz'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

		>>> name = create_string_buffer(b'Samuel')
		>>> name_duplicate = create_string_buffer(10)

		>>> name.raw
		b'Samuel\x00'

		>>> name_duplicate.raw
		b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

		>>> memmove(name_duplicate, name, len(name.value))
		4465608576

		>>> name_duplicate.raw
		b'Samuel\x00\x00\x00\x00'

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —


