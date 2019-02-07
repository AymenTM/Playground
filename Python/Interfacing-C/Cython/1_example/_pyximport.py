#!/usr/local/bin/python3.7

# Compiles Makes Importable all .pyx Files in the Current Directory
# Replacement for the 'setup.py' File
import pyximport; pyximport.install()

import fib
import total
import mathft

# print(fib.fib(30))
# print(fib.fib(30))
# print(fib.fib(30))


print(total.total(30))
