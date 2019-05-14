import urllib.request
from bs4 import BeautifulSoup as bs
from nltk.corpus import stopwords

def processURL(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    print(html)

    

processURL("https://en.wikipedia.org/wiki/SpaceX")