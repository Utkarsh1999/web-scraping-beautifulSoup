from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://en.wikipedia.org/wiki/Shaheed_Sukhdev_College_of_Business_Studies")
bsObj = BeautifulSoup(html.read(),features="html.parser") 
for link in bsObj.find_all('a'):
    print(link.get('href'))

#print("\n\n\ntext from web page : \n\n\n",bsObj.get_text())