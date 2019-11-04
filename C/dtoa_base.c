
#include "IEEE_754_types.h"

char	*ft_dtoa_base(double data, char *base, int width, int precision)
{
	IEEE_754_double flt;
	t_bigint result;
	int32_t exp;

	flt.value = data;
	if IEEE_754_DOUBLE_ZERO(flt.exponent, flt.mantissa)
		result = ft_strdup("0");
	else if IEEE_754_DOUBLE_INF(flt.exponent, flt.mantissa)
		return (flt.sign ? ft_strdup("-inf") : ft_strdup("+inf"));
	else if IEEE_754_DOUBLE_NAN(flt.exponent, flt.mantissa)
		return (flt.mantissa & (1L << (IEEE_754_DOUBLE_MANTISSA_BITS - 1)) ?
			ft_strdup("QNaN") : ft_strdup("SNaN"));
	else if IEEE_754_DOUBLE_SUBNORMALS(flt.exponent, flt.mantissa)
	{
		result = (t_bigint)ft_utoa_base(flt.mantissa, DECIMAL_BASE, 0);
		flt.exponent = -IEEE_754_DOUBLE_BIAS + 1;
	}
	else
	{
		result = (t_bigint)ft_utoa_base(flt.mantissa | IEEE_754_DOUBLE_IMPLICIT_BIT, DECIMAL_BASE, 0);
		flt.exponent -= IEEE_754_DOUBLE_BIAS;
	}
	exp = flt.exponent - IEEE_754_DOUBLE_MANTISSA_BITS;
	if (exp > 0)
		while (exp-- > 0)
			result = bigint_mulfre(result, 2, base, 1);
	else
		while (exp++ < 0)
			result = bigint_divfre(result, 2, base, 1);
	result = bigint_roundfre(result, base, ((precision >= 0) ? precision : 6), 1);
	result = ft_strprepend(result, ft_padding(flt.sign + width - ft_strlen(result), '0'), 1, 1);
	if (flt.sign)
		result = ft_strprepend(result, "-", 1, 0);
	return (result);
}



/* EXPLAINED - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

char	*ft_dtoa_base(double data, char *base, int width, int precision)
{
	IEEE_754_double flt;
	t_bigint result;
	int32_t exp;

	// Extract the Bits of the double Floating-Point Value //
	flt.value = data;

	// Cases //
	if IEEE_754_DOUBLE_ZERO(flt.exponent, flt.mantissa)
	{
		result = ft_strdup("0");
	}
	else if IEEE_754_DOUBLE_INF(flt.exponent, flt.mantissa)
	{
		return (flt.sign ? ft_strdup("-inf") : ft_strdup("+inf"));
	}
	else if IEEE_754_DOUBLE_NAN(flt.exponent, flt.mantissa)
	{
		return (ft_strdup("nan"));
		// return (flt.mantissa & (1L << (IEEE_754_DOUBLE_MANTISSA_BITS - 1)) ?
		// 	ft_strdup("QNaN") : ft_strdup("SNaN"));
	}
	else if IEEE_754_DOUBLE_SUBNORMALS(flt.exponent, flt.mantissa)
	{
		// Convert the mantissa from integer type to (custom) bigint type //
		result = (t_bigint)ft_utoa_base(flt.mantissa, DECIMAL_BASE, 0);
		flt.exponent = -IEEE_754_DOUBLE_BIAS + 1;
	}
	else
	{
		// Convert the mantissa from integer type to (custom) bigint type //
		result = (t_bigint)ft_utoa_base(flt.mantissa | IEEE_754_DOUBLE_IMPLICIT_BIT, DECIMAL_BASE, 0);
		flt.exponent -= IEEE_754_DOUBLE_BIAS;
	}

	// Now we have to correct the position of the mantissa bits by
	 * shifting all of them to the right until the first mantissa
	 * bit is placed at the column that represents 2^-1; that would
	 * mean shifting all the bits as many times as there are mantissa
	 * bits.
	 *
	 * This is because the computer when extracting the bits from the
	 * floating-point type into the unsigned integer, interpreted the
	 * bits in that context, in the context of an integer type, where
	 * each bit is in a column representing a power of two, going from
	 * 0, upward: 2^0, 2^1, 2^2 ... -->
	 *
	 * But we can't do the shift on the unsigned integer type, as that
	 * would cause us to lose the bits past the column representing 2^0,
	 * and we certainly can't store it again in a floating-point type,
	 * AND there is no type that has an encoding where each bit is in a
	 * column representing 2^-1, 2^-2, 2^-3, ... so we must
	 * create a custom type that has that.
	 *
	 * So I went ahead and made one, called it Bigint, you've probably
	 * heard this somewhere before. It's a dynamic string that represents
	 * numbers (in a given base) with characters instead of bits and that
	 * can grow or shrink as much as needed according to the number it is
	 * trying to represent. It is implemented such that it can also represent
	 * numbers with decimals, so where there are columns representing
	 * 10^-1, 10^-2, 10^-3, ... and so on. //

	// We conventiantly add to the exponent the number of shifts to the
	 * right that we must do //
	exp = flt.exponent - IEEE_754_DOUBLE_MANTISSA_BITS;

	// Multiply by the exponent to get rid of the offset that the
	significand is at //
	if (exp > 0)
		while (exp-- > 0)
			result = bigint_mulfre(result, 2, base, 1);
	else
		while (exp++ < 0)
			result = bigint_divfre(result, 2, base, 1);

	// Round to desired precision //
	result = bigint_roundfre(result, base, ((precision >= 0) ? precision : 6), 1);

	// Prepend with 0's as desired //
	result = ft_strprepend(result, ft_padding(flt.sign + width - ft_strlen(result), '0'), 1, 1);

	// Preprend with sign as needed //
	if (flt.sign)
		result = ft_strprepend(result, "-", 1, 0);

	return (result);
}

*/
