
# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —
# Main Part

from distutils.core import setup, Extension

name = 'myModule'
version = '1.0'

module = Extension( name=f'_{name}',
                    sources=[f'{name}.c', f'{name}.i'] )

setup(  name            = name,
        version         = version,
        ext_modules     = [module] )

# NOTE: swig requires an underscore as a prefix for the module
#       extension name (line 10).



# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —
# Hide everything neatly in 1 directory.

import os

os.mkdir(name)
with open(f'{name}/__init__.py', 'x') as f: pass
for file in os.listdir():
    if file != name:
        os.rename(file, f'{name}/{file}')

# You can import the newly created module by specifying
# the name of the directory dot name of module, ex:

# 	  import myModule.myModule as myModule





# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —
# Possible Extension Fields:

# module = Extension(	name 					= 'my_module._module',
#                 	sources 				= ['src/ext_module1.cpp',
#                          		 		   	   'src/ext_module2.cpp',
#                          		 		   	   'src/swig_module.i'],
#                 	swig_opts 				= ['-c++', '-py3'],
#                 	include_dirs 			= [...],
#                 	runtime_library_dirs 	= [...],
#                 	libraries 				= [...],
#                 	extra_compile_args 		= ['-Wno-write-strings'])


# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —
# Possible Setup Fields:

# setup(  name            = '',
#         version         = '',
#         author          = '',
#         author_email    = '',
#         description     = '',
#         license         = '',
#         url             = '',
#         platforms       = ['x86_64'],
#         ext_modules     = [module],
#         packages        = ['my_module'],
#         package_dir     = {'my_module': 'my_module'},
#         package_data    = {'my_module': ['data/*.dat']}
# )


