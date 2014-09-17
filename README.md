
winpeg
------
------

winpeg is a very simple script meant to ease the process of making the most basic
mass file conversions of an entire directory with a specified file extension.

I wrote this script primarily with Windows in mind, hence the name, but it also works
on Linux.

Note: You must have an installation of ffmpeg to use this script.


Installation:
------------
------------

    Linux:

        sudo python2 setup.py install

    Windows:

        python.exe setup.py install

        *Note: Make sure you're using Python 2.7
               Also, if you're downloading the zip make sure to name the extracted folder: winpeg

Example Usage:
-------------
-------------

    winpeg -e flac -c mp3 /home/some_user/some_dir_with_music

    You can optionally delete the original files with the: -do flag

    For Windows users:
        
        Since ffmpeg may not be on the user path and could have been extracted
        anywhere, I've included a single option config file: winpeg.conf which tells you what to add
        Edit that file before usage.

    For a full listing of options run:
        
        winpeg --help
