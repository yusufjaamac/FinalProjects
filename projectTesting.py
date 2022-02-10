# import beautifulsoup4 as beautifulsoup4
# import google as google
from textProcessing import textConvert
# import beautifulsoup4
import google
import requests
from bs4 import BeautifulSoup

#b:[]


def googleSearch():
    try:
        from googlesearch import search

    except ImportError:
        print("Google module not found ")

    # to search
    query = "slack"
    b = []
    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
        b.append(j)
        #print(b)


# put in for loop

#def getLinks():
    # a =[]
    i = 0

    while i < 10:
        # how to get links i google searched above in here to get their html docs
        URL = b[i]
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, "html.parser")
        r = soup.title
        print(b[i])
        print(r.getText) if r else " NO TEXT"
        metadesc = soup.find("meta", property="og:title")
        print(metadesc.getText) if metadesc else " NO META"
        i += 1


#print(b[2])

# print(b[10])

def main():
    print("Hello World!")
    googleSearch()
    #textConvert()

if __name__ == "__main__":
    main()


