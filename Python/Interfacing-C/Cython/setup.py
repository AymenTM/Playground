
from distutils.core import setup
from Cython.Build import cythonize
import os

os.mkdir('pyMod')
for file in os.listdir():

	if os.path.isfile(file) and file.endswith('.pyx'):

		setup(ext_modules=cythonize(file))

		os.system(f'rm {file.split(".")[0]}.c')
		os.system(f'mv build/lib*/*.so pyMod/{file.split(".")[0]}.so')

os.system('rm -r build/')
os.system('touch pyMod/__init__.py')
os.system('clear')
os.system('echo "Process Complete. Output ==>"')
os.system('echo')
os.system('echo "./pyMod"')
os.system('echo "."')
os.system('echo ".."')
os.system('ls -1 pyMod/')
os.system('echo')

