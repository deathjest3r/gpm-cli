gpm-cli - Google Play Music Command Line Interface
==================================================

A command line interface to Google's Play Music service

Installation
------------

Install Google Play Music Python API:
    git clone git://github.com/simon-weber/Unofficial-Google-Music-API.git
    cd Unofficial-Google-Music-API
    git checkout master
    python setup.py install

Install gpm-cli:
    git clone git://github.com/deathjest3r/gpm-cli.git
    cd gpm-cli


Requirements
------------
* Python 2
* gmusicapi
* mplayer
* Some songs on Google Play Music

Usage
-----
`./gpm-cli play "Slayer | Reborn"`

Configuration
-------------
Configuration of gpm-cli is via `~/.gpmrc`. An example config looks like:

            email <your gmailaddress>
            password <your gmail password>

You don't need to store both in the file you can also start gpm-cli without a
config file. Then you have to login manually everytime you start it

Library
-------
The library is stored in `~/.gpm/library.db`. If you want to sync it with the
online library just add `--sync` to the command line

ToDo
----
* Add Media Keys to start/pause/skip tracks
* Add Last.FM plugin
* Sort tracks correcly (by track number)
* Bundle pip package
* Release v0.2 
