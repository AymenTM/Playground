
/*  Template functions.
 *  October 31st, 2019
 */


/* HEADERS  - - - - - - - - - - - - - - - - - - - - - - - - */

#include <limits.h>
#include <stdio.h>
#include <stdint.h>


/* MACROS  - - - - - - - - - - - - - - - - - - - - - - - - - */

#define range___(start, stop, step)              \
	( intmax_t __start__ = (intmax_t)start;  \
		__start__ < (intmax_t)stop;      \
		__start__ += step )

#define range_(start, stop) range___(start, stop, 1)
#define range(stop) range_(0, stop)

#define BIT(i) (1L << i)


/* TEMPLATE FUNCTION  - - - - - - - - - - - - - - - - - - - */

/* Print memory representation of a given value */
#define expose_(T)                                                       \
                                                                         \
	void expose_##T(T val)                                           \
	{                                                                \
		for range(sizeof(T))                                     \
		{                                                        \
			for range(CHAR_BIT) {                            \
				printf("%c", val & BIT(1) ? '1' : '0');  \
			    val >>= 1;                                   \
			}                                                \
			printf(" ");                                     \
		}                                                        \
		printf("\n");                                            \
	}


/* FUNCTION TEMPLATE INSTANTIATION - - - - - - - - - - - - - */

expose_(char)
expose_(short)
expose_(int)
expose_(long)
expose_(__uint128_t)


/* TEST MAIN - - - - - - - - - - - - - - - - - - - - - - - - */

int		main(void)
{
	expose_char         (99);
	expose_short        (999);
	expose_int          (9999);
	expose_long         (99999);
	expose___uint128_t  (999999);

	return (0);
}
