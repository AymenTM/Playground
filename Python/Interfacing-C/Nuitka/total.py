#!/usr/local/bin/python3.7

from sys import argv as av

def total(n):
	y = 0
	for i in range(n + 1):
		y += i
	return y

print(total(int(av[1])))


# Run: python -m nuitka --standalone total.py
