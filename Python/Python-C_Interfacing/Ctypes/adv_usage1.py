#!/usr/local/bin/python3.7

# A More Typical Usage of Ctypes

from ctypes import *


# Import Shared Library
lib = CDLL('./C_simple_example/_clib.so')


# Fix Return Types
lib.add.restype = c_int
lib.sub.restype = c_int
lib.mul.restype = c_int
lib.say_hi.restype = None
lib.say_bye.restype = None


# Wrap Shared Library Functions
def add(a, b):
	return lib.add(c_int(a), c_int(b))

def sub(a, b):
	return lib.sub(c_int(a), c_int(b))

def mul(a, b):
	return lib.mul(c_int(a), c_int(b))


# Use Functions
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
