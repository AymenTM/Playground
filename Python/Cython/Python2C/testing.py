
import timeit

cy = timeit.timeit("example_cy.test(5000)", setup="import example_cy", number=10000)
py = timeit.timeit("example_py.test(5000)", setup="import example_py", number=10000)

print(f'[Cython finished in {cy}]')
print(f'[Python finished in {py}]')
print(f'Cython is {py/cy}x faster than Python')
