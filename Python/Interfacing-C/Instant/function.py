
# Compiling a C source code function at run time

from instant import inline

add = inline("""
int add(int a, int b)
{
    return (a + b);
}
""")

sub = inline("""
int sub(int a, int b)
{
    return (a - b);
}
""")

mul = inline("""
int mul(int a, int b)
{
    return (a * b);
}
""")

print(add(5, 5))
print(sub(5, 5))
print(mul(5, 5))


# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 
# Output:
# 10
# 0
# 25
