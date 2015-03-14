import re, os, time
from urllib2 import urlopen

url_in = "http://www.gutenberg.org/cache/epub/18/pg18.html"
raw_html = 'federalist_full.html'
currated_html = 'federalist_currated.html'
new = 2
