#!/usr/local/bin/python3.7

import logging

# Log calls of severity 'level' and above
logging.basicConfig(level=logging.DEBUG)

# Silences logging calls of severity 'level' and below
logging.disable(level=logging.CRITICAL)

x = input('Enter in a number: ')
logging.debug(f'{x} is of type {type(x)}')

y = input('Enter in another number: ')
logging.debug(f'{y} is of type {type(y)}')

print(f'The sum of {x} and {y} is {x + y}')
