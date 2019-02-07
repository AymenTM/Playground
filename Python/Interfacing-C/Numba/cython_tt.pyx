
# Writing the 'total' Function in Cython (i.e in C)

cpdef int cy_total(int n):
	cdef int y, i
	y = 0
	for i in range(n + 1):
		y += i
	return y
