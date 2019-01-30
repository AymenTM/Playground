
import timeit

cy = timeit.timeit("myModule.fib(30)", setup="import myModule", number=1)
py = timeit.timeit("pyModule.pyFib(30)", setup="import pyModule", number=1)

print(f'[Cython finished in {cy}]')
print(f'[Python finished in {py}]')
print(f'Cython is {py/cy}x faster than Python')
