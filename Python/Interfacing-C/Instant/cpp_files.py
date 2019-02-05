
# Compiling a C++ Source Code File into a Python Module at
# Run Time and then Importing it

from instant import build_module

build_module(  modulename                = 'libcpp',

               source_directory          = './CPP_example',
               include_dirs              = ['./CPP_example'],

               sources                   = ['source1.cpp',
                                            'source2.cpp'],

               local_headers             = ['source3.h'],
               system_headers            = ['iostream'],

               additional_declarations   = r'%include "source3.h"',

               cppargs                   = ['-O3'] )

import libcpp

print(libcpp.add(5, 5))
print(libcpp.sub(5, 5))
print(libcpp.mul(5, 5))
libcpp.say_hi()
libcpp.say_bye()
libcpp.say_done()

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 
# Output:
# Done!
# 10
# Done!
# 0
# Done!
# 25
# Hello, world!
# Bye, world!
# Done!
