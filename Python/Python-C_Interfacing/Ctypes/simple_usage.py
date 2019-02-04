#!/usr/local/bin/python3.7

# Importing and using a Shared C Library

import ctypes

lib = ctypes.CDLL('./C_simple_example/_clib.so')

print(lib.add(5, 5))
print(lib.sub(5, 5))
print(lib.mul(5, 5))
lib.say_hi()
lib.say_bye()

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 
# Output:
# 10
# 0
# 25
# Hello, world!
# Bye, world!
