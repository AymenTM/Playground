
# Calling C Library Functions

from libc cimport stdlib, string

cpdef int atoi(char *s):
	return stdlib.atoi(s)

cpdef int strlen(char *s):
	return string.strlen(s)

cpdef char *strstr(char *haystack, char *needle):
	return string.strstr(haystack, needle)

