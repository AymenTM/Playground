#!/usr/local/bin/python3.7

from ctypes import *

lib = CDLL('./C_byref_example/_lib.so')

lib.ft_strcpy.restype = None

def strcpy(buffer):
	return





