from urllib.request import urlopen 
from bs4 import BeautifulSoup 
html = urlopen("http://www.wikipedia.org/") 
# while(True) :
bsObj = BeautifulSoup(html.read(),features="html.parser") 
print(bsObj.head.meta) 
