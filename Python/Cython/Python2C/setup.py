
files = [
	'example_cy.pyx'
]

from distutils.core import setup
from Cython.Build import cythonize

for file in files:
	setup(ext_modules=cythonize(file))

# run the command: 'python setup.py build_ext --inplace'
