#!/usr/local/bin/python3.7

import pyximport ; pyximport.install()

import cy_examples
import cy_types
import libc

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

# cy_examples.hi()
# cy_examples.hi1()
# cy_examples.foo(50, b'Jason')
# cy_examples.total(100)

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

# cy_types.print_variables()
# cy_types.print_variable_arrays()

# a = 100
# b = 5

# print(cy_types.ft_divmod1(a, b))
# print(cy_types.ft_divmod3(a, b))

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

# print(libc.atoi(b'2147483647'))
# print(libc.strlen(b'2147483647'))
print(libc.strstr(b'2147483647', b'48'))
print(libc.strstr(b'', b'48'))

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —
