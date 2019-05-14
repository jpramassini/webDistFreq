import urllib.request
from bs4 import BeautifulSoup as bs
from nltk.corpus import stopwords
from nltk import FreqDist

def processURL(url):
    '''
    Retrieve raw html from passed url.
    :param url: the url to fetch the html at.
    '''
    response = urllib.request.urlopen(url)
    html = response.read()
    return html

def tokenizeText(html):
    '''
    Parses html into text and returns it as a tokenized array.
    :param html: the html code to parse.
    :return: array of tokens from parsed html. 
    '''
    soup = bs(html, "html5lib")
    text = soup.text
    tokens = [t for t in text.split()]
    return tokens

def calcFreqDist(tokens):
    cleaned_tokens = tokens[:]
    for token in tokens:
        if token in stopwords.words('english') or not token.isalpha():
            cleaned_tokens.remove(token)

    #print(set(tokens) - set(cleaned_tokens))
    freq = FreqDist(cleaned_tokens)
    # for key,val in freq.items():
    #     print(str(key) + ':' + str(val))
    freq.plot(20, cumulative=False)
    

def main():
    loop = True
    while loop == True:
        url = input("Paste url here: ")
        try:
            calcFreqDist(tokenizeText(processURL(url)))
        except Exception as e: print(e)
        response = input("Would you like to enter another url? (y/n) ")
        yesses = ["y", "Y"]
        if not response in yesses:
            loop = False

if __name__ == "__main__":
    main()