import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/Siddharthanagar'
page = requests.get(URL)

def get_citations_needed_count(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all(class_= 'noprint Inline-Template Template-Fact')
    print (len(results))

def get_citations_needed_report(URL):
    page = requests.get(URL)
    '''
    BeautifulSoup can parse many types of content.
    # We're parsing html so let BeautifulSoup know
    # conventionally you store the BeatifulSoup instance in a variable named soup
  '''
    soup = BeautifulSoup(page.content, 'html.parser')

    '''
      here we're finding all elements with the given class
     NOTE: use class_ since class by itself is a Python keyword
     '''
    paragraphs = soup.find_all(class_= 'noprint Inline-Template Template-Fact')

    # result of find_all is iterable and can be used in for loops

    for citations in paragraphs:
        print(citations.parent.text)

# calling both functions
get_citations_needed_count(URL)
get_citations_needed_report(URL)