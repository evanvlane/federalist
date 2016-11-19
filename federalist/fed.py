import re, os, time
from urllib2 import urlopen
import fedmessages

url = "http://www.gutenberg.org/cache/epub/18/pg18.html"
rawHtml = "fedFull.html"
finalHtml = "fedCurrated.html"
template = "./templates/fedTemplate.html"

defaultList = [1, 2, 6, 9, 10, 15, 23, 39, 49, 50, 51, 57, 62, 63, 68, 69, 76, 78, 84]

print(fedmessages.welcomeMsg)

if not os.path.isfile(os.path.abspath(rawHtml)):
	print(fedmessages.retrieveMsg)

	fed = open(os.path.abspath(rawHtml), "w")
	fed.write(urlopen(url).read())
	fed.close()

	print(fedmessages.retrieveSuccess)
else:
	print(fedmessages.localRetrieveMsg)

currated = open(os.path.abspath(finalHtml), "w")
print(fedmessages.fileOpenMsg)

with open(template,"r") as f:
	currated.write(f.read())

papers = raw_input(fedmessages.inputMsg)

if len(papers) == 0:
	papers = defaultList
else:
	while True:
		try: 
			papers = map(int, papers.split())
			break
		except ValueError:
			papers = raw_input(fedmessages.inputErrorMsg)

with open(rawHtml, 'r') as f:
	text = f.read()

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

currated.write(fedmessages.footer % time.strftime("%m/%d/%Y"))
currated.close()