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



# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —




# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —




