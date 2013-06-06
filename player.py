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
        self._stop = threading.Event()

    def play(self, track):
        try:
            player = gst.element_factory_make("playbin2", "player")
            player.set_property("uri", track)
            player.set_state(gst.STATE_PLAYING)
            while True:
                time.sleep(10)
        except KeyboardInterrupt:
            pass
            #sys.exit(0)
    
    def pause(self):
        pass

    def stop(self):
        try:
            if isinstance(self._proc, subprocess.Popen):
                self._proc.communicate("stop\n")
            self._stop.set()
        except ValueError:
            pass

    def next(self):
        try:
            if isinstance(self._proc, subprocess.Popen):
                self._proc.terminate()
        except OSError:
            pass

    def prev(self):
        pass
