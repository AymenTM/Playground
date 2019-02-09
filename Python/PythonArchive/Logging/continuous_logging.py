#!/usr/local/bin/python3.7

import logging
import time

logging.basicConfig(filename='logging.txt', level=logging.DEBUG)

while 1:
	logging.debug('Data ...')
	time.sleep(1)


# Then from another terminal run: 'tail -f <logfile>' to
# see the constant flow of logging data being appended to
# the log file.
