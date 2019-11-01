/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ctest.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: akharrou <akharrou@student.42.us.org>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/10/31 21:50:54 by akharrou          #+#    #+#             */
/*   Updated: 2019/10/31 23:19:31 by akharrou         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/*
**    NAME
**         expose_T -- stringify underlying memory representation
**
**    SYNOPSIS
**         #include <libft.h>
**
**         char *expose_integral( void *integral, size_t size, int oflags );
**
**         char *expose_8bit( __int8_t data, int flags );
**         char *expose_16bit( __int16_t data, int flags );
**         char *expose_32bit( __int32_t data, int flags );
**         char *expose_64bit( __int64_t data, int flags );
**         char *expose_128bit( __int128_t data, int flags );
**
**         MACRO --  char *expose_char( char data, int oflags );
**         MACRO --  char *expose_short( short data, int oflags );
**         MACRO --  char *expose_int( int data, int oflags );
**         MACRO --  char *expose_long( long data, int oflags );
**         MACRO --  char *expose_llong( long long data, int oflags );
**
**         char *expose_float( float data, int oflag );
**         char *expose_double( double data, int oflag );
**         char *expose_ldouble( long double data, int oflag );
**
**    PARAMETERS
**
**         T data                lvalue or rvalue of type T.
**
**         int oflags            The oflag argument may indicate the
**                               spacing of bytes, the endianness desired
**                               and whether or not to truncate
**                               insignificant trailing 0s.
**
**                               Default is unspaced and big endian
**                               representation.
**
**                               The flags specified for the oflag
**                               argument are formed by or'ing the
**                               following values:
**
**                               O_DEFAULT          not spaced & in big
**                                                  endianness
**
**                               O_SPACED           bytes or major sections
**                                                  are spaced
**
**                               O_TRUNCATE         truncate insignificant
**                                                  0's at the end
**
**                               O_LITTLE_ENDIAN    little-endian representation
**                               O_BIG_ENDIAN       big-endian representation
**
**    DESCRIPTION
**         Allocates a null terminated string equivalent to the number of bits
**         that form the underlying memory representation for the given type T.
**         Then proceeds to filling the string with all the bits that represent
**         the value (of type T).
**
**    RETURN VALUES
**         Returns a the memory representation as a null-terminated string.
*/


/* HEADERS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */

#include <limits.h>
#include <stdint.h>
#include <stdio.h>


/* MACROS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */

#define BIT(i) (1L << i)


/* PROTOTYPES - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */

char		*expose_integral(void *integral, size_t size, int oflags);

char		*expose_8bit(__int8_t data, int flags);
char		*expose_16bit(__int16_t data, int flags);
char		*expose_32bit(__int32_t data, int flags);
char		*expose_64bit(__int64_t data, int flags);
char		*expose_128bit(__int128_t data, int flags);

char		*expose_float(float data, int oflag);
char		*expose_double(double data, int oflag);
char		*expose_ldouble(long double data, int oflag);

# define	expose_char(data, flags) expose_8bit  (data, flags)
# define	expose_short(data, flags) expose_16bit (data, flags)
# define	expose_int(data, flags) expose_32bit (data, flags)
# define	expose_long(data, flags) expose_64bit (data, flags)
# define	expose_llong(data, flags) expose_64bit (data, flags)


/* ENUMS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */

enum e_expose_function_suite_flags
{
	O_DEFAULT       = 0,
	O_SPACED        = (1 << 0),
	O_TRUNCATE      = (1 << 1),
	O_LITTLE_ENDIAN = (1 << 2),
	O_BIG_ENDIAN    = (1 << 3),
};


/* FUNCTION DEFINITIONS - - - - - - - - - - - - - - - - - - - - - - - - - - - */

char	*expose_8bit(__int8_t data, int flags)
{
	__int8_t tmp;

	tmp = data;
	return (expose_integral(&tmp, sizeof(__int8_t), flags));
}

char	*expose_16bit(__int16_t data, int flags)
{
	__int16_t tmp;

	tmp = data;
	return (expose_integral(&tmp, sizeof(__int16_t), flags));
}

char	*expose_32bit(__int32_t data, int flags)
{
	__int32_t tmp;

	tmp = data;
	return (expose_integral(&tmp, sizeof(__int32_t), flags));
}

char	*expose_64bit(__int64_t data, int flags)
{
	__int64_t tmp;

	tmp = data;
	return (expose_integral(&tmp, sizeof(__int64_t), flags));
}

char	*expose_128bit(__int128_t data, int flags)
{
	__int128_t tmp;

	tmp = data;
	return (expose_integral(&tmp, sizeof(__int128_t), flags));
}

char	*expose_integral(void *integral, size_t size, int oflags)
{
	char	*buf;
	size_t	bufsize;
	size_t	cur_idx;
	ssize_t	i;

	bufsize = ((oflags & O_SPACED) ? size - 1 : 0) + size * CHAR_BIT + 1;
	cur_idx = bufsize;
	if (!(buf = malloc(bufsize)))
		return (NULL);
	buf[--cur_idx] = '\0';
	while (cur_idx)
	{
		i = 0;
		while (i < CHAR_BIT)
			buf[--cur_idx] = *(char *)integral & BIT(i++) ? '1' : '0';
		++integral;
		if ((oflags & O_SPACED) && cur_idx)
			buf[--cur_idx] = ' ';
	}
	if (oflags & O_TRUNCATE)
	{
		while (buf[cur_idx] != '1')
			++cur_idx;
		memmove(buf, &(buf[cur_idx]), bufsize - cur_idx);
	}
	if (oflags & O_LITTLE_ENDIAN)
		ft_strrev(buf);
	return (buf);
}

char	*expose_float(float data, int oflag)
{
	char	*buf;
	size_t	bufsize;
	size_t	i;
	union {
		float val;
		struct {
			uint64_t mantissa : 23;
			uint64_t exp      : 8;
			uint64_t sign     : 1;
		} info;
	} flt;

	flt.val = data;
	bufsize = sizeof(float) * 8 + ((oflag & O_SPACED) ? 2 : 0) + 1;
	if (!(buf = malloc(bufsize)))
		return (NULL);
	buf[--bufsize] = '\0';
	i = 0;
	while (i < 23)
		buf[--bufsize] = flt.info.mantissa & BIT(i++) ? '1' : '0';
	if (oflag & O_SPACED)
		buf[--bufsize] = ' ';
	i = 0;
	while (i < 8)
		buf[--bufsize] = flt.info.exp & BIT(i++) ? '1' : '0';
	if (oflag & O_SPACED)
		buf[--bufsize] = ' ';
	buf[--bufsize] = flt.info.sign ? '1' : '0';
	if (oflag & O_LITTLE_ENDIAN)
		ft_strrev(buf);
	return (buf);
}

char	*expose_double(double data, int oflag)
{
	char	*buf;
	size_t	bufsize;
	size_t	i;
	union {
		double val;
		struct {
			uint64_t mantissa : 52;
			uint64_t exp      : 11;
			uint64_t sign     : 1;
		} info;
	} flt;

	flt.val = data;
	bufsize = sizeof(double) * 8 + ((oflag & O_SPACED) ? 2 : 0) + 1;
	if (!(buf = malloc(bufsize)))
		return (NULL);
	buf[--bufsize] = '\0';
	i = 0;
	while (i < 52)
		buf[--bufsize] = flt.info.mantissa & BIT(i++) ? '1' : '0';
	if (oflag & O_SPACED)
		buf[--bufsize] = ' ';
	i = 0;
	while (i < 11)
		buf[--bufsize] = flt.info.exp & BIT(i++) ? '1' : '0';
	if (oflag & O_SPACED)
		buf[--bufsize] = ' ';
	buf[--bufsize] = flt.info.sign ? '1' : '0';
	if (oflag & O_LITTLE_ENDIAN)
		ft_strrev(buf);
	return (buf);
}

char	*expose_ldouble(long double data, int oflag)
{
	char	*buf;
	size_t	bufsize;
	size_t	i;
	union {
		long double val;
		struct {
			uint64_t mantissa : 63;
			uint64_t exp      : 15;
			uint64_t explicit : 1;
			uint64_t sign     : 1;
		} info;
	} flt;

	flt.val = data;
	bufsize = 80 + ((oflag & O_SPACED) ? 2 : 0) + 1;
	if (!(buf = malloc(bufsize)))
		return (NULL);
	buf[--bufsize] = '\0';
	i = 0;
	while (i < 63)
		buf[--bufsize] = flt.info.mantissa & BIT(i++) ? '1' : '0';
	if (oflag & O_SPACED)
		buf[--bufsize] = ' ';
	buf[--bufsize] = flt.info.explicit ? '1' : '0';
	i = 0;
	while (i < 15)
		buf[--bufsize] = flt.info.exp & BIT(i++) ? '1' : '0';
	if (oflag & O_SPACED)
		buf[--bufsize] = ' ';
	buf[--bufsize] = flt.info.sign ? '1' : '0';
	if (oflag & O_LITTLE_ENDIAN)
		ft_strrev(buf);
	return (buf);
}


/* TEST MAIN - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */

int main(int ac, char **av)
{

	printf("char:    %s\n", expose_char    (99     , O_SPACED /* | O_TRUNCATED | O_LITTLE_ENDIAN | O_BIG_ENDIAN */) );
	printf("short:   %s\n", expose_short   (999    , O_SPACED /* | O_TRUNCATED | O_LITTLE_ENDIAN | O_BIG_ENDIAN */) );
	printf("int:     %s\n", expose_int     (9999   , O_SPACED /* | O_TRUNCATED | O_LITTLE_ENDIAN | O_BIG_ENDIAN */) );
	printf("long:    %s\n", expose_long    (99999  , O_SPACED /* | O_TRUNCATED | O_LITTLE_ENDIAN | O_BIG_ENDIAN */) );
	printf("llong:   %s\n", expose_llong   (999999 , O_SPACED /* | O_TRUNCATED | O_LITTLE_ENDIAN | O_BIG_ENDIAN */) );
	printf("\n");

	printf("float:   %s\n", expose_float   (6.25, O_SPACED /* | O_LITTLE_ENDIAN | O_BIG_ENDIAN */) );
	printf("double:  %s\n", expose_double  (6.25, O_SPACED /* | O_LITTLE_ENDIAN | O_BIG_ENDIAN */) );
	printf("ldouble: %s\n", expose_ldouble (6.25, O_SPACED /* | O_LITTLE_ENDIAN | O_BIG_ENDIAN */) );

	(void)ac;
	(void)av;

    return (0);
}

/* OUTPUT:

char:    01100011
short:   00000011 11100111
int:     00000000 00000000 00100111 00001111
long:    00000000 00000000 00000000 00000000 00000000 00000001 10000110 10011111
llong:   00000000 00000000 00000000 00000000 00000000 00001111 01000010 00111111

float:   0 10000001 10010000000000000000000
double:  0 10000000001 1001000000000000000000000000000000000000000000000000
ldouble: 0 1000000000000010 100100000000000000000000000000000000000000000000000000000000000

*/
