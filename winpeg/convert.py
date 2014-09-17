# Imports
import subprocess
import os
from contextlib import closing
from sys import exit
import json

# Author and licensing
__Author__ = "b-mcg" 
__Email__ = "b.mcg0890@gmail.com"
__License__ = """
Copyright (C) 2014-2016 b-mcg <b.mcg0890@gmail.com>
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""
# Version number
VERSION = 'v0.0.1' 


def convert_contents(glob_object, args):
    """
    Loops through specific files in a directory
    and converts them to another format and optionally
    deletes the original files.

    glob_object -- glob object returned from iglob
    args        -- dictionary of command line argument values

    """

    # Unix type system so ffmpeg is already in path
    if os.name == 'posix':

        ffmpeg_args     =   ['ffmpeg', '-i']

    # Windows system so ffmpeg may not be on path
    elif os.name == 'nt':

        # Read in the path from the config file
        try:

            with closing(open(os.path.abspath("{0}\\{1}".format(os.path.expanduser('~'), 'winpeg\\winpeg.conf')), 'r')) as fil:

                conf = json.loads(fil.read())
                path = conf['ffmpeg_path']
            
            ffmpeg_args     =   [path, '-i']

        except IOError:

            print "\nError: could not open file for reading.  Make sure the base directory is named winpeg.\n"
            exit(1)

    # Loop through files, convert them, and delete original files if -do option was given
    for f in glob_object:

        copied_args = ffmpeg_args[:]
        copied_args.extend([f, f.replace(f.split('.')[-1], args['c'])])

        try:
            subprocess.call(copied_args)

        except:
            print "\nError: The ffmpeg program is required.\n"
            exit(2)

        if args['del']:

            try:
                os.remove(f)

            except:

                print "\nError: Unable to delete original file.\n"
                continue

