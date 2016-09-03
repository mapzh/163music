#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'mapengzhen'

from HTMLParser import HTMLParser

class SongParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag=="img":
            if len(attrs) == 2:
                print attrs
                if cmp(attrs[0], ('class', 'j-flag')) == 0:
                    print attrs[1]
            else:
                pass
