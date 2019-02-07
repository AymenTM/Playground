#!/usr/local/bin/python3.7

# File to Test Numba v.s Python

import pyximport ; pyximport.install()

import timeit

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

nmba = timeit.timeit("example.numba_total(5000)", setup="import example", number=10000)
py = timeit.timeit("example.py_total(5000)", setup="import example", number=10000)
cy = timeit.timeit("cython_tt.cy_total(5000)", setup="import cython_tt", number=10000)

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

print(f'[Python finished in {py}]')
print(f'[Numba finished in {nmba}]')
print(f'[Cython finished in {cy}]')

print()

print(f'Numba is {py/nmba}x faster than Python')
print(f'Cython is {py/cy}x faster than Python')
print(f'Cython is {nmba/cy}x faster than Numba')

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

# # OUTPUT:

# [Python finished in 6.745206788]
# [Numba finished in 0.4079922370000002]
# [Cython finished in 0.0020303540000004006]

# Numba is 16.532684145164254x faster than Python
# Cython is 3322.1826282503785x faster than Python
# Cython is 200.94635566010643x faster than Numba

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —
