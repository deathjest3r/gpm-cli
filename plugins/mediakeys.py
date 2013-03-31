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

from Xlib.display import Display
from Xlib import X
import sys

from plugin import plugin

class mediakeys(plugin):
    def __init__(self):
        plugin.__init__(self)

    def handle_event(event):
        print "key pressed"

    def run(self):
        display = Display()
        screen = display.screen()
        root = screen.root

        while True:
            #event = root.display.next_event()
            #if event.type in [X.KeyPress, X.KeyRelease]:
            #    handle_event(event)
            if self.stopped():
                break
