import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://www.goodreads.com/book/title.xml?author=Arthur+Conan+Doyle&key=0cyzaC4tvlHtrXh3L1vxA&title=Hound+of+the+Baskervilles').read()
soup = bs.BeautifulSoup(source,'json')

print(soup)
