import re, os, time
from urllib2 import urlopen

url_in = "http://www.gutenberg.org/cache/epub/18/pg18.html"
raw_html = 'federalist_full.html'
currated_html = 'federalist_currated.html'
new = 2


print """
============================================================================
Welcome to the Federalist Papers Reader.
From here you can generate a currated selection of whichever papers interest you.
The default list is the 2008 reading list for St. John's College, Santa Fe.
============================================================================

"""


if not os.path.isfile('%s' % os.path.abspath(raw_html)):
	print "Please wait a moment while the program retrieves the full text from Project Gutenberg:"
	fed = open(os.path.abspath(raw_html),"w")
	fed.write(urlopen(url_in).read())
	fed.close()
	print "File Downloaded Successfully"
	currated = open(os.path.abspath(currated_html), "w")
else:
	print "Opening the local copy of the Federalist Papers:"	
	currated = open(os.path.abspath(currated_html), "w")
	print "File Opened Succesfully"

currated.write("""
<?xml version='1.0' encoding='UTF-8'?>
<!DOCTYPE html PUBLIC '-//W3C//DTD XHTML 1.1//EN' 'http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd'>
<html xmlns="http://www.w3.org/1999/xhtml">
  <head><title>Selections from the Federalist Papers </title>

<style type="text/css">
.pageno       { position: absolute; right: 95%; font: medium sans-serif; }
.pageno:after { color: gray; content: '[' attr(title) ']' }
.toc-pageref  { float: right }
pre           { font-family: monospace; font-size: 0.9em; white-space: pre-wrap }
/*
Theme Name: zh2
Theme URI: http://zenhabits.net/theme/
Author: Leo Babauta
Author URI: http://leobabauta.com
Description: A minimalist, content-focused theme.
Version: 2
License: Uncopyrighted
License URI: http://zenhabits.net/open-source-blogging-feel-free-to-steal-my-content/

This theme is uncopyrighted.
Do whatever you'd like with it.
*/

/* css reset */


html, body, div, span, applet, object, iframe,
h1, h2, h3, h4, h5, h6, p, blockquote, pre,
a, abbr, acronym, address, big, cite, code,
del, dfn, em, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, var,
b, u, i, center,
dl, dt, dd, ol, ul, li,
fieldset, form, label, legend,
table, caption, tbody, tfoot, thead, tr, th, td,
article, aside, canvas, details, embed, 
figure, figcaption, footer, header, hgroup, 
menu, nav, output, ruby, section, summary,
time, mark, audio, video {
	margin: 0;
	padding: 0;
	border: 0;
	font-size: 100%;
	font: inherit;
	vertical-align: baseline;
}
/* HTML5 display-role reset for older browsers */
article, aside, details, figcaption, figure, 
footer, header, hgroup, menu, nav, section {
	display: block;
}
body {
	line-height: 1;
}
ol, ul {
	list-style: none;
}
blockquote, q {
	quotes: none;
}
blockquote:before, blockquote:after,
q:before, q:after {
	content: '';
	content: none;
}
table {
	border-collapse: collapse;
	border-spacing: 0;
}
/* end css reset */

@media all { 
	em{
	font-style: italic;
	}
	#fedcontent {
	position: relative;
	left: 50%;
	width: 960px;
	margin-left: -480px;
	}
	body {
	    font: normal 100% Open Sans,Helvetica,sans-serif;
	    background-color: #fff;
	    color: #000;
	    padding: .6em;
	    -webkit-font-smoothing: antialiased;
	}
	/* fades out blog title */
	.top {
	    -webkit-opacity: 0.30;
	    -moz-opacity: 0.30;
	    opacity: 0.30;
	    -webkit-transition: opacity 3s linear;
	    -moz-transition: opacity 3s linear;
	    -ms-transition: opacity 3s linear;
	    -o-transition: opacity 3s linear;
	    transition: opacity 3s linear;
	}
	/* fades blog title back in on hover */
	.top:hover {
	    -webkit-opacity: 1;
	    -moz-opacity: 1;
	    opacity: 1;
	    -webkit-transition: all 2s ease;
	    -moz-transition: all 2s ease;
	    -ms-transition: all 2s ease;
	    -o-transition: all 2s ease;
	    transition: all 2s ease;
	}
	.container {
	    overflow: hidden;
	    padding: 0 1em;
	    max-width: 42.5em;
	    margin: auto;
	}
	/* blog title */
	h1 {
	    font-size: 150%;
	    font-weight: normal;
	    color: #d3d3d3;
	    letter-spacing: .01em;
	    margin: 0 .05em 0 0;
	    text-align: center;
	}
	h1 a:link {
	    color: #d3d3d3;
	    text-decoration: none;
	    border-width: 0 0 1px 0;
	    border-style: none none solid none;
	    border-color: #c0c0c0;
	}
	h1 a:visited {
	    color: #d3d3d3;
	    text-decoration: none;
	    border-width: 0 0 1px 0;
	    border-style: none none solid none;
	    border-color: #c0c0c0;
	}
	h1 a#tagline { color: #56a49f }
	/* post title */
	h2 {
	    font-family: 'Sorts Mill Goudy', Georgia, Times, serif;
	    font-size: 3.5em;
	    color: #333;
	    font-weight: normal;
	    margin-top: 1em;
	    text-align: center;
	    line-height: 1.3em;
	}
	/* subtitles */
	h3 {
	    font-family: 'Sorts Mill Goudy', Georgia, Times, serif;
	    font-size: 2.5em;
	    color: #666;
	    font-weight: normal;
	    line-height: 1em;
	    margin-top: 1.5em;
	    text-align: center;
	}
	h3.subtitle { 
	    margin-top: .5em;
	}
	h4 {
	    font-family: 'Sorts Mill Goudy', Georgia, Times, serif;
	    font-size: 1.5em;
	    line-height: 1.2em;
	    color: #666;
	}
	/* used for "edit" link only visible to site owner/writers */
	h5 {
	    font-family: 'Sorts Mill Goudy', Georgia, Times, serif;
	    font-size: 2.5em;
	    color: #666;
	    font-weight: normal;
	    line-height: 1em;
	    margin-top: 1.5em;
	    text-align: center;
	}
	/* author credits */
	h6 {
	    font-size: 1.5em;
	    font-weight: normal;
	    line-height: 1.3em;
	    color: #666;
	    font-family: 'Sorts Mill Goudy', Georgia, Times, serif;
	    margin: 1em 0 .5em 0;
	    letter-spacing: .1em;
	    margin-bottom: 1em;
	    text-align: center;
	    -webkit-opacity: 0.30;
	    -moz-opacity: 0.30;
	    opacity: 0.30;
	    -webkit-transition: opacity 3s linear;
	    -moz-transition: opacity 3s linear;
	    -ms-transition: opacity 3s linear;
	    -o-transition: opacity 3s linear;
	    transition: opacity 3s linear;
	}
	/* fades author credit back in on hover */
	h6:hover {
	    -webkit-opacity: 1;
	    -moz-opacity: 1;
	    opacity: 1;
	    -webkit-transition: all 2s ease;
	    -moz-transition: all 2s ease;
	    -ms-transition: all 2s ease;
	    -o-transition: all 2s ease;
	    transition: all 2s ease;
	}
	h6 strong {
	    color: #56a49f;
	    font-weight: bold;
	}
	img {
	    border: 0;
	    padding: 3px;
	}
	img a { border: 0 }
	p {
	    line-height: 1.635em;
	    margin: .7em 0 1em 0;
	    font-family: 'Cardo', Georgia, Cambria, 'Times New Roman', Times, serif;
	    font-size: 1.3em;
	    color: #333;
	    -webkit-font-smoothing: antialiased;
	}
	a:link {
	    color: #333;
	    text-decoration: none;
	    border-width: 0;
	    border-style: none;
	}
	a:visited {
	    color: #333;
	    text-decoration: none;
	    border: 0;
	    border-width: 0;
	    border-style: none;
	}
	a:hover {
	    color: #999;
	    text-decoration: none;
	    border: 0;
	    border-width: 0;
	    border-style: none;
	}
	/* post styles */
	.post strong { font-weight: bold }
	.post em { font-style: italic }
	.post a:link {
	    color: #303030;
	    text-decoration: none;
	    border-width: 0 0 1px 0;
	    border-style: none none solid none;
	    border-color: #c0c0c0;
	}
	.post a:visited {
	    color: #303030;
	    text-decoration: none;
	    border-width: 0 0 1px 0;
	    border-style: none none solid none;
	    border-color: #c0c0c0;
	}
	.post a:hover {
	    color: #999;
	    border-width: 0 0 1px 0;
	    border-style: none none solid none;
	    border-color: #c0c0c0;
	    text-decoration: none;
	}
	.post ul {
	    list-style-type: disc;
	    padding: .1em .0 0 1.1em;
	    margin-top: .5em;
	    margin-bottom: 1em;
	    font-family: 'Cardo', Georgia, Cambria, 'Times New Roman', Times, serif;
	    font-size: 1.3em;
	    -webkit-font-smoothing: antialiased;
	}
	.post ol {
	    list-style-type: decimal;
	    padding: .1em 0 0 1.2em;
	    margin-top: .5em;
	    margin-bottom: 1em;
	    font-family: 'Cardo', Georgia, Cambria, 'Times New Roman', Times, serif;
	    font-size: 1.3em;
	    -webkit-font-smoothing: antialiased;
	}
	.post li {
	    line-height: 1.5em;
	    padding: .2em 0 0 0;
	    color: #333;
	}
	.post li strong { font-weight: bold }
	.post blockquote {
	    border-left: 2px solid #a5abab;
	    font-size: 1.1em;
	    margin: 1.8em .8em;
	    padding: 0 1em 0 1em;
	    color: #666;
	    font-family: Open Sans,Helvetica,sans-serif;
	}
	/* line at bottom of post */
	.home_bottom {
	    border-bottom: 1px solid #efefef;
	    font-family: Open Sans,Helvetica,sans-serif;
	    font-size: 2em;
	    line-height: 2.5em;
	    color: #dedede;
	}
	/* previous & next posts at bottom */
	.navigation { margin-bottom: 3em }
	.navigation p {
	    text-transform: uppercase;
	    color: #666;
	    font-size: .7em;
	    letter-spacing: .2em;
	    font-family: Open Sans,Helvetica,sans-serif;
	    font-weight: bold;
	    margin-top: 0;
	    margin-bottom: 1em;
	}
	/* subscription */
	.subscribe p {
	    text-transform: uppercase;
	    color: #666;
	    font-size: 1em;
	    letter-spacing: .2em;
	    font-family: Open Sans,Helvetica,sans-serif;
	    font-weight: bold;
	    line-height: 2em;
	    margin-top: 2em;
	    margin-bottom: 2em;
	}
	/* "see all posts" at bottom of home page */
	.all_posts {
	    font-size: 2.4em;
	    font-weight: bold;
	    height: 1.25em;
	    line-height: 1.25em;
	    margin-bottom: 1em;
	}
	.all_posts a { color: #d3d3d3 }
	.all_posts a:visited { color: #d3d3d3 }
	.all_posts a:hover { color: #666 }
	/* footer text */
	.footer p {
	    font-size: .8em;
	    letter-spacing: .2em;
	    text-transform: lowercase;
	    color: #333;
	    padding: 0;
	    margin: 0;
	    margin-left: 0;
	    padding-left: 0;
	    font-family: Open Sans,Helvetica,sans-serif;
	}
	.footer a { color: #666 }
	/* for archives page */
	#arc {
	    overflow: hidden;
	    margin: 0 1em 2em .4em;
	}


}

/* for iPad-sized devices */
@media only screen and (max-device-width: 800px) { 
	/* makes blog title not fade on touch screen */
	.top {
	    margin: auto;
	    -webkit-opacity: 1;
	    -moz-opacity: 1;
	    opacity: 1;
	}
	h6 {
	    -webkit-opacity: 1;
	    -moz-opacity: 1;
	    opacity: 1;
	}
	.navigation p { font-size: 1em }
	.subscribe ul {
	    margin-top: 4em;
	    font-size: 1.8em;
	}
	.footer p { font-size: 1.2em }
	h2 { font-size: 2.5em }
	h3 { font-size: 2em }
	h6 { font-size: 1.5em }
	p {
	    font-size: 1.5em;
	    line-height: 1.5em;
	}
	.post ul {
	    font-size: 1.5em;
	    line-height: 1em;
	    padding: .1;
	}
	.post ol {
	    font-size: 1.5em;
	    line-height: 1em;
	    padding: .1;
	}
	#arc {
	    font-size: 1.2em;
	}
}

/* for narrower browsers */
@media screen and (max-width: 800px) { 
	/* makes blog title not fade on touch screen */
	.top {
	    margin: auto;
	    -webkit-opacity: 1;
	    -moz-opacity: 1;
	    opacity: 1;
	}
	h6 {
	    -webkit-opacity: 1;
	    -moz-opacity: 1;
	    opacity: 1;
	}
	.navigation p { font-size: 1em }
	subscribe ul {
	    margin-top: 4em;
	    font-size: 1.8em;
	}
	.footer p { font-size: 1.2em }
	h2 { font-size: 2.5em }
	h3 { font-size: 2em }
	h6 { font-size: 1.5em }
	p {
	    font-size: 1.5em;
	    line-height: 1.5em;
	}
	.post ul {
	    font-size: 1.5em;
	    line-height: 1em;
	    padding: .1;
	}
	.post ol {
	    font-size: 1.5em;
	    line-height: 1em;
	    padding: .1;
	}
}

/* for iPhone-sized devices */
@media only screen and (max-device-width: 480px) { 
	.container { width: auto }
	body { padding: 0 }
	h1 { font-size: 2em }
	h2 { font-size: 2.5em }
	h3 { font-size: 1.8em }
	h6 { font-size: 1.3em }
	p {
	    font-size: 1.2em;
	    line-height: 1.4em;
	}
	.post ul {
	    list-style-type: disc;
	    list-style-position: inside;
	    font-size: 1.2em;
	    line-height: 1em;
	    padding: .5em;
	    margin: 0;
	}
	.post ol {
	    list-style-position: inside;
	    font-size: 1.2em;
	    line-height: 1em;
	    padding: .5em;
	    margin: 0;
	}
	.post li {
	    margin: 0;
	}
	/* makes blog title not fade on touch screen */
	.top {
	    -webkit-opacity: 1;
	    -moz-opacity: 1;
	    opacity: 1;
	}
	.navigation p { font-size: 1.5em }
	h6 {
	    -webkit-opacity: 1;
	    -moz-opacity: 1;
	    opacity: 1;
	}
	.subscribe p {
	    font-size: 1em;
	    margin-top: 1em;
	}
	.footer p { font-size: 1em }
}	
@media print {
	body{
	position: absolute !important;
	width: auto !important;
	}
	div, p, #footer{
	    font-family: Helvetica,sans-serif !important;
	    font-size: 14px !important;
	    background: white !important;
	    color: black !important;
		margin: 0 !important;
		left: 0 !important;
	}
	.container { display: block }
	.navigation { display: none }
	.subscribe { display: none }
	.footer { display: none }
}



</style>
</head>
  <body><div id="fedcontent">

<h2>Selections from The Federalist Papers</h2> 
<h1>by Alexander Hamilton and John Jay and James Madison</h1>

""")

papers = raw_input('Please input which papers you want, separated by spaces (ENTER for default list): ')

if len(papers) == 0:
	papers = [1, 2, 6, 9, 10, 15, 23, 39, 49, 50, 51, 57, 62, 63, 68, 69, 76, 78, 84]
else:
	while True:
		try:
			papers = map(int, papers.split())
			break
		except ValueError:
			papers = raw_input('Sorry, they all need to be integers. Please try again: ') 
	
text = file(raw_html, "r").read()

for i, val in enumerate(papers):
	reString = '(?<=No. ' + str(papers[i]) + '</p>)(.*)(?=<p id=.*No. '+str(papers[i]+1)+'</p>)'
	print(reString)
	m = re.findall( reString, text, re.DOTALL)
	m = str(m[0])
	m = m.replace('\r\n\r\n','')
	m = m.replace('\r\n',' ')
	#print(m)
	currated.write("""<h2> Federalist No. %d</h2>""" % val)
	currated.write(str(m))
	
currated.write("""
<br>
<h4 id="footer">This selection of the <em>Federalist Papers</em> was generated on %s. The source text is from an OCR scan made available through <a href="http://www.gutenberg.org">Project Gutenberg</a> and the styling is courtesy of <a href="http://www.zenhabits.net">Zen Habits</a>. The script was written in Python 2.7 by <a href="mailto:evanvlane@gmail.com?Subject=Federalist 20Papers Script">Evan Lane</a> (SJCSF '10).</h4>
</div>
</body>
</html>
""" % time.strftime("%m/%d/%Y"))
currated.close()

load_page = raw_input('If you would like to open the document enter "Y": ')

if load_page == 'Y' or load_page == 'y':
	if os.name =='nt':
		os.system('start %s' %os.path.abspath(currated_html))
	else:
		os.system('open %s' %os.path.abspath(currated_html))
	
	
