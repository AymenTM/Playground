#!/bin/sh

# Don't forget to configure your 'setup.py' file correctly.

python3.7 setup.py build

# mv build/lib*/*.so .
# rm -rf build
# mv *.so $(echo $(echo *.c | cut -d . -f1).so)

# — — — — — — — — — — — — — — — — — — — — — — — —
# Possible Commands:

#    pythonX setup.py build								~Builds into cwd~
#    pythonX setup.py install --instal-platlib=.        ~Installs module into cwd~
#    pythonX setup.py install                           ~Installs module into python folder~
