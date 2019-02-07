#!/usr/local/bin/python3.7

from pyximport import install ; install()

import my_libc
import PYX_Modules.nothing as nt

my_libc.hello('James')	  			# C File Function
print(my_libc.strlen('James'))   	# C File Function
nt.say_hi()				  			# Cython File Function
