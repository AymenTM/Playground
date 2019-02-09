#!/usr/local/bin/python3.7

# Example of launching the PDB Debugger with the
# built-in 'breakpoint()' function.


y = 0

breakpoint()
for i in range(100):
	y += i
	print(f'Incrementing y={y} by i={i} ...')
	print('Done!')

print(y)



# Once in the PDB Debugger:

# 	> typing 'help' : brings out the list of all the available PDB commands
#  	> typing 'help' <command> : brings out the documentation of the specified command
