#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Get in the flow.

Starts Youtube video on all chromecast connected devices
and sends a wake on lan packet to a computer that is turned off.

"""
import pychromecast
import webbrowser
import requests
from wakeonlan import wol

__author__ = 'Mikael Kall'
__email__ = 'kall.micke@gmail.com'

"""Youtube link to play"""
YOUTUBE_URL = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
"""Mac address for wake on lan"""
MACADDR = 'f4:b7:e2:0d:d4:c0'


class Flow:
    """All flow definitions."""

    global YOUTUBE_URL
    global MACADDR

    def __init__(self):
        """Set instance variables from global variables."""
        self.youtube_url = YOUTUBE_URL
        self.youtube_id = YOUTUBE_URL.split('?')[1]
        self.macaddr = MACADDR

    def stream_youtube(self):
        """Stream youtube to every chromecast connected to the network."""
        for chromecast_info in pychromecast.discover_chromecasts():
            (address, port, uuid, tp, desc) = chromecast_info
            self.__puts('info', "Chromecast [%s] detected" % (address))
            url = "http://%s:8008/apps/YouTube" % (address)
            self.__puts('success', "Streams %s" % (url))
            head = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            requests.post(url, self.youtube_id, headers=head)

    def browse_youtube(self):
        """Open youtube in webbrowser."""
        self.__puts('success', "Browsing youtube: %s" % (self.youtube_url))
        controller = webbrowser.get()
        controller.open(self.youtube_url)

    def start_computer(self):
        """Start computer that it's turned off."""
        self.__puts('success', "Sends wakeon lan packet [%s]" % (self.macaddr))
        wol.send_magic_packet(self.macaddr)

    def __puts(self, tp, msg):
        """Output messages in fancy colors."""
        if tp == "info":
            print("%s%s%s" % ('\033[93m', "➜ ", msg))
        elif tp == "warning":
            print("%s%s%s" % ('\033[93m', "➜ ", msg))
        elif tp == "error":
            print("%s%s%s" % ('\033[91m', "✖ ", msg))
        elif tp == "success":
            print("%s%s%s" % ('\033[92m', "✔ ", msg))


if __name__ == '__main__':

    flow = Flow()
    flow.stream_youtube()
    flow.browse_youtube()
    flow.start_computer()
