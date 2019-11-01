
import os
from distutils.core import setup, Extension
name = 'libcpp'
swig_cmd =r'swig -python -py3 -I/Users/aymenkh/Library/Python/3.7/lib/python/site-packages/instant/swig -I.. -c++ -fcompact -O -I. -small -py3 libcpp.i'
os.system(swig_cmd)
sources = ['source1.cpp', 'source2.cpp', 'libcpp_wrap.cxx']

setup(name = 'libcpp',
      ext_modules = [Extension('_' + 'libcpp',
                     sources,
                     include_dirs=['./CPP_example'],
                     library_dirs=[],
                     libraries=[] , extra_compile_args=['-O3'] )])
