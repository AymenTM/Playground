
#include "myModule.h"

int fib(int n)
{
    if (n < 2)
        return (n);
    else
        return (fib(n - 1) + fib(n - 2));
}

int my_mod(int n, int m)
{
  return(n % m);
}
