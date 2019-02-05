#!/usr/local/bin/python3.7

from ctypes import *

lib = CDLL('./C_byref_example/lib.so')

lib.ft_strcpy.restype = None



def ft_strcpy(dest, src):
	lib.ft_strcpy(dest, src)

def ft_divmod(a, b, div_ptr, mod_ptr):
	lib.divmod(c_int(a), c_int(b), div_ptr, mod_ptr)


# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 

name = create_string_buffer(b'John')
dup = create_string_buffer(len(name.value))

print(dup.raw)
ft_strcpy(dup, name)
print(dup.raw)

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 

a = 100
b = 5
div = c_double()
mod = c_double()

ft_divmod(a, b, byref(div), byref(mod))

print(f'{div}')
print(f'{mod}')
print(f'{a} / {b} = {div.value}')
print(f'{a} % {b} = {mod.value}')

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 
