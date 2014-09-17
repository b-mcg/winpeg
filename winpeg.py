#!/usr/bin/env python2

# Imports
import argparse
import winpeg.convert as convert
from glob import iglob
import os

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


def build_opts():
    """
    Returns a parser object of command line arguments.

    """

    parser  =   argparse.ArgumentParser(description='winpeg command line options')

    # Add directory argument
    parser.add_argument('directory', type=str, help='Directory to glob for all files matching a specified extension', metavar='')

    # Add extension type argument
    parser.add_argument('-e', '--extension', type=str, required=True,
                        help='File extension to search for in glob pattern Ex: <flac>', metavar='')

    # Add conversion type argument
    parser.add_argument('-c', '--convert', type=str, default='mp3', help='The file type to convert to Ex: <avi> (Default: mp3)', metavar='')

    # Add delete original flag
    parser.add_argument('-do', action='store_true', default=False, required=False,
                        help='Delete original files after converted')

    return parser

def arg_parser(parser):
    """
    Returns a dictionary of parsed
    command line arguments.

    """

    args    =   parser.parse_args()

    return {'dir' : args.directory,
            'c'   : args.convert,
            'e'   : args.extension,
            'del' : args.do
            }

def main():
    """
    main()

    Parses command line arguments and
    converts files in a directory.

    """

    args            =   arg_parser(build_opts())

    dir_contents    =   iglob('{0}/*.{1}*'.format(os.path.abspath(args['dir']), args['e']))

    convert.convert_contents(dir_contents, args)


if __name__ == '__main__':

    print "\nwinpeg {0} running ...\n".format(VERSION)

    main()

    print "\n"
