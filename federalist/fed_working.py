#! /usr/bin/python3

import re
import os
from urllib2 import urlopen

url_in = "http://www.gutenberg.org/cache/epub/18/pg18.html"
raw_html = 'federalist_full.html'
currated_html = 'federalist_currated.html'

# TODO Implement basic structure

class GutBook(object):


if not os.path.isfile('%s' % os.path.abspath(raw_html)):

        print("Please wait a moment while the program retrieves the full text from Project Gutenberg:")
        fed = open(os.path.abspath(raw_html), "w")
        fed.write(urlopen(url_in).read())
        fed.close()
        print("File Downloaded Successfully")
        currated = open(os.path.abspath(currated_html), "w")
else:
        print("Opening the local copy of the Federalist Papers:")
        currated = open(os.path.abspath(currated_html), "w")


if __name__ == "__main__":
    pass
