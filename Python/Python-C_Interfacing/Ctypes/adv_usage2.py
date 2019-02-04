#!/usr/local/bin/python3.7

# A More Typical Usage of Ctypes

import ctypes


# Import Shared Library
_libc = ctypes.CDLL('./C_adv_example/_fib.so')


# Fix Return Types
_libc.fib.restype = ctypes.c_int


# Wrap Shared Library Functions
def fib(index):
	return _libc.fib(ctypes.c_int(index))


# Use Functions
print(fib(40))
