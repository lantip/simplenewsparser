#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests import get
from readability.readability import Document
import re
import logging
requests_log = logging.getLogger("requests")
requests_log.setLevel(logging.WARNING)
URL = raw_input('What url should I read? :' + '\n')

def get_news(href):
    rec = ''
    l = get(href)
    readable_article = Document(l.text).summary(html_partial=True)
    readable_title = Document(l.text).title()
    rec = readable_title + readable_article
    return rec

print get_news(URL)
