
# setup.py

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import os

C_dirname = 'C_Library' 	  # Directory that Contains All C Source Files

pyx_sources = [file for file in os.listdir() if file.endswith('.pyx')]
modules = [Extension("my_libc", pyx_sources)]

setup(	name 		 = 'Cython Library',
		cmdclass 	 = {'build_ext': build_ext},
		ext_modules  = modules )

os.system('mv *.so $(echo *.so | cut -d. -f1,3)')
os.system('rm -rf *.c build/')
os.system('clear ; echo "Process Complete —>" *.so')
