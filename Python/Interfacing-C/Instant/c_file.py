
# Compiling a C source code file at run time

from instant import build_module

with open('./C_example/source.c') as f:
	lib = build_module(	code = f.read() )

print(lib.add(5, 5))
print(lib.sub(5, 5))
print(lib.mul(5, 5))
lib.say_hi()
lib.say_bye()

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 
# Output:
# 10
# 0
# 25
# Hello, world!
# Bye, world!
