
# Compiling a C source code module at run time

from instant import build_module

lib = build_module(code=r"""

#include <stdio.h>

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

void say_hi(void)
{
    printf("Hello, world!\n");
}

void say_bye(void)
{
    printf("Bye, world!\n");
}
""")


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
