#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests import get
from BeautifulSoup import BeautifulSoup
import re
URL = raw_input('What url should I read? :' + '\n')

def get_news(href):
    rec = ''
    l = get(href)
    dl = BeautifulSoup(l.text)
    rec = dl.findAll(['title', 'content', 'p'])
    return rec

print get_news(URL)
