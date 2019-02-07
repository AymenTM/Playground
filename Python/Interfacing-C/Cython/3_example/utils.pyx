
# utils.pyx

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

cpdef strlen(object name):

	cdef extern from "C_Library/utils.c":
		int ft_strlen(char *s)

	return ft_strlen(bytes(name, encoding = 'utf-8'))

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

cpdef hello(object name):

	cdef extern from "C_Library/other.c":
		void ft_hello(char *name)

	return ft_hello(bytes(name, encoding = 'utf-8'))

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —


# take a look here for details about different Cython declarations
# http://notes-on-cython.readthedocs.io/en/latest/function_declarations.html
