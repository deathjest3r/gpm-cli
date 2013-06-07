# This file is part of the gpm-cli.
#
# Copyright (C) 2013 Death Jester <d3ath.jest3r@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301 USA

import os, sys, time
import subprocess
import threading

import pygst
pygst.require("0.10")
import gst

class Player:
    def __init__(self, sound_dev = "alsa:device=hw=0.0"):
        self._proc = None
        self.sound_dev = sound_dev

    def play(self, track):
        try:
            self._player = gst.element_factory_make("playbin2", "player")
            self._player.set_property("uri", track)
            self._player.set_state(gst.STATE_PLAYING)
            self._state = 'play' 
            while True:
                if self._state != 'play':
                    self._player.set_state(gst.STATE_NULL)
                    return self._state
                time.sleep(1)
        except KeyboardInterrupt:
            sys.exit(0)
    
    def pause(self):
        if self._player.get_state(0)[1] == gst.STATE_PLAYING:
            self._player.set_state(gst.STATE_PAUSED)
        else:
            self._player.set_state(gst.STATE_PLAYING)

    def stop(self):
        self._state = 'stop'

    def next(self):
        self._state = 'next'

    def prev(self):
        self._state = 'prev'
