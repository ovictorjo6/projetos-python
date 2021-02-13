import requests
import pandas as pd 
from bs4 import BeautifulSoup

def getdata(url):
    r = requests.get(url)
    return r.text

#inserir pessoa de interesse 
htmldata = getdata('https://pt.wikipedia.org/wiki/Karl_Marx')

soup = BeautifulSoup(htmldata,'html.parser')

data = ''

for data in soup.find_all("p"):
    print(data.get_text())