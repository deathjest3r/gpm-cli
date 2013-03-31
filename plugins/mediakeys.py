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

from Xlib import X
from Xlib.error import BadAccess
from Xlib.display import Display

from plugin import plugin

keys = [172,  # XF86AudioPlay
        174,  # XF86AudioStop
        171,  # XF86AudioNext
        173 ] # XF86AudioPrev

class mediakeys(plugin):
    def __init__(self, player):
        plugin.__init__(self)
        
        self._player = player
        self._keybind_failed = False

    def handle_event(self, event):
        keycode = event.detail
        if keycode in keys:
            # Play/Pause key
            if keycode == 172:
                self._player.play()
            # Stop key
            elif keycode == 174: 
                self._player.stop()
            # Next key
            elif keycode == 171:
                self._player.next()
            # Prev key
            elif keycode == 173:
                self._player.prev()

    # We have to register our own exception handler since Xlib does not catch
    # exceptions correctly
    def handle_xerror(self, err, req = None):
        if isinstance(err, BadAccess):
            self._keybind_failed = True
        else:
            self.display.default_error_handler(err)

    def run(self):
        self.display = Display()
        root = self.display.screen().root

        self.display.set_error_handler(self.handle_xerror)
        
        root.change_attributes(event_mask = X.KeyPressMask)
        for keycode in keys:
            root.grab_key(keycode, X.AnyModifier, 1, X.GrabModeAsync,
                    X.GrabModeAsync)
      
        self.display.sync()
        if self._keybind_failed:
            print "Can't enable 'mediakeys', already in use by an other process"
            return

        while True:
            event = root.display.next_event()
            self.handle_event(event)
            if self.stopped():
                break
            
