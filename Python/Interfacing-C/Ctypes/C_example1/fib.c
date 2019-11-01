
/* C Library Containing Fibonacci Function */

int fib(int index)
{
	if (index < 2)
		return (index);
	return (fib(index - 1) + fib(index - 2));
}
