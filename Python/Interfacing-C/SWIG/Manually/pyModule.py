def pyFib(index):
    return index if index < 2 else (pyFib(index - 1) + pyFib(index - 2))
