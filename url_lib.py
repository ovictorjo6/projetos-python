from urllib.request import urlopen

open_url = urlopen('https://pt.wikipedia.org/wiki/Karl_Marx')
webcontent = open_url.read()
print(webcontent)
