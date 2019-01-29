
from distutils.core import setup
from Cython.Build import cythonize
import os

for file in os.listdir():

	if os.path.isfile(file) and file.endswith('.pyx'):

		setup(ext_modules=cythonize(file))
		os.system('mv build/lib*/*.so . ; rm -rf build *.c')
