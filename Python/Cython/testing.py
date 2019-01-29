import timeit

c = timeit.timeit("ctotal.total(5000)", setup="import ctotal", number=10000)
cy = timeit.timeit("cytotal.total(5000)", setup="import cytotal", number=10000)
py = timeit.timeit("pytotal.pytotal(5000)", setup="import pytotal", number=10000)

print(f'[C finished in {c}]')
print(f'[Cython finished in {cy}]')
print(f'[Python finished in {py}]')

print(f'C is {cy/c}x faster than Cython and {py/c}x faster than Python')
print(f'Cython is {py/cy}x faster than Python')
