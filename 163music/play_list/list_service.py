#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'mapengzhen'

import urllib2
import song_parser
import song

class ListService():
    def get_play_list(self):
        url = "http://music.163.com/#/discover/playlist/"
        response = urllib2.urlopen(url)
        self.response = response.read()
        self.parse_songs()

    def parse_songs(self):
        parser = song_parser.SongParser()
        parser.feed(self.response)
