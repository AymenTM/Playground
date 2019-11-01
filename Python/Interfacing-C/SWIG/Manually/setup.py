from distutils.core import setup, Extension

module = Extension("myModule", sources = ["myModule.c"])

setup(
        name ="PackageName",
        description="This is a package for myModule.",
        ext_modules = [module]
)
