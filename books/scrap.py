import bs4 as bs
import urllib.request


def get_rating(isbn):
    add='https://www.goodreads.com/book/isbn/'+str(isbn)+'?key=0cyzaC4tvlHtrXh3L1vxA'
    source = urllib.request.urlopen(add).read()
    soup = bs.BeautifulSoup(source,'lxml')
    rating = soup.ratings_count.string
    return rating
