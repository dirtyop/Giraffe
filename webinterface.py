import urllib
import urllib.request
from bs4 import BeautifulSoup


url = 'http://www.dr-chuck.com/page1.htm'
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('href',None))

