
import timeit

cy = timeit.timeit("myModule.fib(30)", setup="import myModule", number=1)
py = timeit.timeit("myPyModule.pyFib(30)", setup="import myPyModule", number=1)

print(f'[Cython finished in {cy}]')
print(f'[Python finished in {py}]')
print(f'Cython is {py/cy}x faster than Python')
