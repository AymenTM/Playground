
# Compiling a C source code module at run time

from instant import build_module

c_code = """
int add(int a, int b)
{
    return (a + b);
}

int sub(int a, int b)
{
    return (a - b);
}

int mul(int a, int b)
{
    return (a * b);
}
"""

mathlib = build_module(code=c_code)

print(mathlib.add(5, 5))
print(mathlib.sub(5, 5))
print(mathlib.mul(5, 5))

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 
# Output:
# 10
# 0
# 25




c_code = r"""
#include <stdio.h>

void say_hi(void)
{
    printf("Hello, world!\n");
}

void say_bye(void)
{
    printf("Bye, world!\n");
}
"""

lib = build_module(code=c_code)
lib.say_hi()
lib.say_bye()

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 
# Output:
# Hello, world!
# Bye, world!
