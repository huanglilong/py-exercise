#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import stdio
from instream import InStream

def _readHTML(word):
    WEBSITE = 'http://cn.bing.com/dict/search?q=' + word + '&qs=n&form=Z9LH5&sp=-1&pq=fade&sc=8-4&sk=&cvid=61497272101D4A1BBF2F5B03FFDABA52'
    page = InStream(WEBSITE)
    html = page.readAll()
    return html

def wordTranslator(word):
    html = _readHTML(word)
    uStr = '释义'.decode('utf-8')
    begin = html.find(unicode(uStr), 0)
    end = html.find('"', begin)
    translator = html[begin:end]
    return translator

def main():
    word = sys.argv[1]
    translator = wordTranslator(word)
    stdio.writeln(translator)

if __name__ == '__main__':
    main()

