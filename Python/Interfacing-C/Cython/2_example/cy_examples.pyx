
# Testing a Couple of Functions

from collections import OrderedDict


def foo(int i, char *name):
    print(name)
    return (i + i)

def hi():
    print('hello world')

cpdef void hi1():
    print('hello world')

cpdef int total(int x):
    cdef int y = 0
    cdef int i
    for i in range(x):
        y += i
    return y

cdef class Cheese:

    cdef double width, height

    def __init__(self, w, h):
        self.width = w
        self.height = h

    def describe(self):
        print(f"Cheese is {self.width} by {self.height}")

class Student:

    def __init__(self, name, age, level):
        self.name = name
        self.age = age
        self.level = level

    def describe(self):
        print(f"My name is {self.name}. I'm {self.age} yrs old")
