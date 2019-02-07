#!/usr/local/bin/python3.7

from numba import jit

def py_total(n):
	y = 0
	for i in range(n + 1):
		y += i
	return y

@jit
def numba_total(n):
	y = 0
	for i in range(n + 1):
		y += i
	return y

# print(py_total(10000000))
# print(numba_total(10000000))
