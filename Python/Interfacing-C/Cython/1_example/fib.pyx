
cpdef int fib(int index):
    return index if index < 2 else fib(index - 1) + fib(index - 2)
