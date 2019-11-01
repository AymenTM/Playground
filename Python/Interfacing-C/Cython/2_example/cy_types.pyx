
from __future__ import print_function

cpdef void print_variables():

	cdef bint old = True
	cdef int age = 4
	cdef double rate = 4.72
	cdef float change = 4.72
	cdef char *name = 'James'
	cdef list students = ['Steve', 'John', 'Peter', 'Sam']
	cdef set nationalities = {'Turkish', 'French', 'Canadian', 'American'}
	cdef tuple levels = ('Freshman', 'Freshman', 'Sophmore', 'Senior')
	cdef dict sizes = {'small':'5feet', 'medium':'6feet', 'large':'7feet', 'xlarge':'8feet'}

	print(f'Bint 	—>   {old}',
		  f'Int 	—>   {age}',
		  f'Double  —>   {rate}',
		  f'Float 	—>   {change}',
		  f'Char* 	—>   {name}',
		  f'List 	—>   {students}',
		  f'Set 	—>   {nationalities}',
		  f'Tuple 	—>   {levels}',
		  f'Dict    —> 	 {sizes}',
		  sep="\n")


cpdef void print_variable_arrays():

	cdef int int_arr[10]
	int_arr[0] = 3
	int_arr[1] = 2
	int_arr[2] = 1
	int_arr[3] = 0

	print(f'int_arr[0] 	—>   {int_arr[0]}',
		  f'int_arr[1] 	—>   {int_arr[1]}',
		  f'int_arr[2] 	—>   {int_arr[2]}',
		  f'int_arr[3] 	—>   {int_arr[3]}',
		  sep="\n")
