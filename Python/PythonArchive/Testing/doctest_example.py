#!/usr/local/bin/python3.7

import doctest

def addTwoNumbers(a, b):
	'''
	Returns the sum of the two integers a and b.

	>>> addTwoNumbers(2, 2)
	4
	>>> addTwoNumbers(2, 4)
	6
	>>> addTwoNumbers(4, 6)
	11
	'''
	return int(a) + int(b)

doctest.testmod()

# or just run: 'python -m doctest <script>.py' from the terminal
