
# Script Version 1.0

from contextlib import contextmanager
from distutils.core import setup, Extension
import os

@contextmanager
def gotoDirectory(path):
    try:
        initial_dir = os.getcwd()
        os.chdir(path)
        yield
    finally:
        os.chdir(initial_dir)

# Fetch Module Names
files = []
version = '1.0'
for directory in os.listdir():
    if os.path.isdir(directory):
        files.append((directory, version))

os.mkdir('pyMod')
for name, version in files:

    with gotoDirectory(name):

        module = Extension( name=f'_{name}',
                            sources=[f'{name}.c', f'{name}.i'] )

        setup(  name            = name,
                version         = version,
                ext_modules     = [module] )

        os.system('mv *.py ./build/lib*/*.so ../pyMod/')
        os.system('rm -rf ./build *_wrap.c')

os.system('touch pyMod/__init__.py')
os.system('clear')
os.system('echo "Process Complete. Output ==>"')
os.system('echo')
os.system('echo "./pyMod"')
os.system('echo "."')
os.system('echo ".."')
os.system('ls -1 pyMod/')
os.system('echo')


# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —














# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —
# # Main Part

# from contextlib import contextmanager
# from distutils.core import setup, Extension
# import os

# @contextmanager
# def gotoDirectory(path):
#     try:
#         initial_dir = os.getcwd()
#         if os.path.isdir(path) is False:
#             os.mkdir(path)
#         os.chdir(path)
#         yield
#     except Exception:
#         raise 'Error in "gotoDirectory"'
#     finally:
#         os.chdir(initial_dir)

# # Manually Set the Module Names
# # files = [
# #     ('myFib', '1.0'),
# #     ('myStrlen', '1.0'),
# #     ('myConvertBase', '1.0')
# # ]

# # Automatically Sets the Module Names
# files = []
# version = '1.0'
# for directory in os.listdir():
#     if os.path.isdir(directory):
#         files.append((directory, version))

# # Duplicate Everything into a Seperate Directory
# cpy_dir = 'Recreate'
# os.mkdir(cpy_dir)
# for file in os.listdir():
#     if file != cpy_dir:
#         os.system(f'cp -r {file} {cpy_dir}/{file}')


# for name, version in files:

#     # If your files are already in seperate directories than comment this out
#     # Move everything related to 'name' to a Temporary Directory
#     # os.mkdir(name)
#     # for file in os.listdir():
#     #     if file != name and file.split('.')[0] == name:
#     #         os.system(f'mv {file} {name}/{file}')

#     # # Cd to that Seperate Directory
#     with gotoDirectory(name):

#         # Build
#         module = Extension( name=f'_{name}',
#                             sources=[f'{name}.c', f'{name}.i'] )

#         setup(  name            = name,
#                 version         = version,
#                 ext_modules     = [module] )

#         # NOTE: swig requires an underscore as a prefix for the module
#         #       extension name (line 48).

#         # Extract the Necessary Files & Clean Up
#         os.system('mv ./build/lib*/*.so .')
#         os.system('rm -r build/ *.c *.h *.i')
#         os.system('mv * ../')

#     os.system(f'rm -r {name}')

# os.system('rm setup.py')
# with open(f'__init__.py', 'x') as f: pass
# final_dir = 'pyModule'
# os.mkdir(final_dir)
# os.system(f'mv * {final_dir}')





# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —
# Possible Extension Fields:

# module = Extension(   name                    = 'my_module._module',
#                   sources                 = ['src/ext_module1.cpp',
#                                              'src/ext_module2.cpp',
#                                              'src/swig_module.i'],
#                   swig_opts               = ['-c++', '-py3'],
#                   include_dirs            = [...],
#                   runtime_library_dirs    = [...],
#                   libraries               = [...],
#                   extra_compile_args      = ['-Wno-write-strings'])


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


