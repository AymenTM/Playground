
#include "ctotal.h"

int ctotal(int x)
{
	int y = 0;

	for (int i = 0; i < x; i++)
		y += i;
	return (y);
}
