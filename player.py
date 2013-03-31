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

import os
import subprocess

class Player:
    def __init__(self, sound_dev = "alsa:device=hw=0.0"):
        self._proc = None
        self.sound_dev = sound_dev

    def start(self, stream_url):
        try:
            with open(os.devnull, 'w') as temp:
                self._proc = subprocess.Popen(["mplayer", "-slave", "-ao", \
                        self.sound_dev, "%s" % stream_url],
                        stdin=subprocess.PIPE, stdout=temp, stderr=temp)
                
                self._proc.wait()
        except KeyboardInterrupt:
            try:
                if not self._proc.poll():
                    self._proc.terminate()
            except OSError:
                print "Can't close mplayer"
            raise KeyboardInterrupt 

    def play(self):
        try:
            if not self._proc.poll():
                self._proc.communicate("pause\n") 
        except ValueError:
            pass

    def stop(self):
        try:
            if not self._proc.poll():
                self._proc.communicate("stop\n")
        except ValueError:
            pass

    def next(self):
        try:
            if not self._proc.poll():
                self._proc.terminate()
        except OSError:
            pass # Already terminated

    def prev(self):
        pass
