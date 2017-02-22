#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

import setuptools

def main():

    setuptools.setup(
        name             = "ophanim",
        version          = "2017.02.22.2343",
        description      = "monitoring and notifications for measurements such as Bitcoin value and internet connection security",
        long_description = long_description(),
        url              = "https://github.com/wdbm/ophanim",
        author           = "Will Breaden Madden",
        author_email     = "wbm@protonmail.ch",
        license          = "GPLv3",
        py_modules       = [
                           "ophanim"
                           ],
        install_requires = [
                           "denarius",
                           "propyte",
                           "shijian"
                           ],
        scripts          = [
                           "ophanim.py"
                           ],
        entry_points     = """
            [console_scripts]
            ophanim = ophanim:ophanim
        """
    )

def long_description(
    filename = "README.md"
    ):

    if os.path.isfile(os.path.expandvars(filename)):
        try:
            import pypandoc
            long_description = pypandoc.convert_file(filename, "rst")
        except ImportError:
            long_description = open(filename).read()
    else:
        long_description = ""
    return long_description

if __name__ == "__main__":
    main()
