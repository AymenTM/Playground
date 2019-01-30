
# Script Version 2.0

# See "../dirsOnly" for Version 0.1
# See Version 1.0 below

from distutils.core import setup, Extension
import os

files = []
version = '1.0'
for file in os.listdir():
    if os.path.isfile(file) and file.endswith('.c'):
        files.append((file.split('.')[0], version))

for name, version in files:

    module = Extension( name=f'_{name}',
                        sources=[f'{name}.c', f'{name}.i'] )

    setup(  name            = name,
            version         = version,
            ext_modules     = [module] )

    os.system('mv build/lib*/*.so .')

os.system('rm -rf *_wrap.c build/')
os.system('mkdir pyMod')
os.system('touch pyMod/__init__.py')
os.system('mv *.py *.so pyMod/')
os.system('mv pyMod/setup.py .')
os.system('clear')
os.system('echo "Process Complete. Output ==> pyMod"')




# Script Version 1.0

# See "../dirsOnly" for Version 0.1

# from distutils.core import setup, Extension
# import os

# files = []
# version = '1.0'
# for file in os.listdir():
#     if os.path.isfile(file) and file.endswith('.c'):
#         files.append((file.split('.')[0], version))

# os.system(f'mkdir Recreate')
# for name, version in files:

#     module = Extension( name=f'_{name}',
#                         sources=[f'{name}.c', f'{name}.i'] )

#     setup(  name            = name,
#             version         = version,
#             ext_modules     = [module] )

#     os.system('mv build/lib*/*.so .')

#     os.system(f'mv {name}.c Recreate/')
#     os.system(f'mv {name}.h Recreate/')
#     os.system(f'mv {name}.i Recreate/')

# os.system('rm -rf *_wrap.c build/')
# os.system(f'mv setup.py Recreate/')
