#!/usr/bin/env python2

# Imports
from setuptools import setup
from shutil import copyfile, rmtree
import os

import winpeg

pathname    =   os.getcwd()

VERSION     =   '0.0.1'

copyfile("winpeg.py", "winpeg/winpeg")

packages    =   ["winpeg"]

setup(
        name            =   "winpeg",
        version         =   VERSION,
        description     =   ("Simple script to use ffmpeg for mass conversion of directory."),
        author          =   "b-mcg",
        author_email    =   "b.mcg0890@gmail.com",
        url             =   "https://www.github.com/b-mcg/winpeg",
        packages        =   packages,
        package_dir     =   {"winpeg" : os.path.abspath(os.path.join(pathname, "winpeg/"))},
        scripts         =   ["winpeg/winpeg"],
        data_files      =   [("share/winpeg", ["README.md", "LICENSE"])],
        )

try:

    rmtree(os.path.abspath(os.path.join(pathname, "build/")))
    rmtree(os.path.abspath(os.path.join(pathname, "dist/")))
    rmtree(os.path.abspath(os.path.join(pathname, "winpeg.egg-info/")))

except:

    pass
