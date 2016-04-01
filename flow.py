#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'kall.micke@gmail.com'

import pychromecast
import webbrowser
import requests

'''
 Youtube link to play.
'''
YOUTUBE_URL = 'http://www.youtube.com/watch?v=oT3mCybbhf0'


class Flow:

    global YOUTUBE_URL

    def __init__(self):

        self.youtube_url = YOUTUBE_URL
        self.youtube_id = YOUTUBE_URL.split('?')[1]

    def stream_youtube(self):

        '''
          Streams youtube to every chromecast connected to the network.
        '''
        for chromecast_info in pychromecast.discover_chromecasts():
            (address, port, uuid, tp, desc) = chromecast_info
            self.__puts('info', "Chromecast [%s] detected" % (address))
            url = "http://%s:8008/apps/YouTube" % (address)
            self.__puts('success', "Streams %s" % (url))
            head = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            r = requests.post(url, self.youtube_id, headers=head)

    def browse_youtube(self):
        '''
         Opens youtube in webbrowser.
        '''
        self.__puts('success', "Browsing youtube: %s" % (self.youtube_url))
        controller = webbrowser.get()
        controller.open(self.youtube_url)

    def __puts(self, tp, msg):
        '''
         Outputs messages in fancy colors.
        '''
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
