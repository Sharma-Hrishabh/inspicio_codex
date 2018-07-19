import bs4 as bs
import urllib.request

add='https://www.goodreads.com/book/isbn/'+'0441172717'+'?key=0cyzaC4tvlHtrXh3L1vxA'
source = urllib.request.urlopen(add).read()
soup = bs.BeautifulSoup(source,'lxml')

print(soup.ratings_sum.string)
