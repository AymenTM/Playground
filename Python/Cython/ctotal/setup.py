
from distutils.core import setup, Extension

files = [
    ('ctotal', '1.0')
]

for name, version in files:

    module = Extension( name=f'_{name}',
                        sources=[f'{name}.c', f'{name}.i'] )

    setup(  name            = name,
            version         = version,
            ext_modules     = [module] )
