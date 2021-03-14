import requests

url = 'Enter image url here'

r = requests.get(url)

#image .jpg
path = 'img.jpg'

with open (path, "wb") as f:
	f.write(r.content)
