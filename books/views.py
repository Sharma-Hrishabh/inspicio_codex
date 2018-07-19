from django.shortcuts import render,redirect
from .models import Book
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from books.config import pagination
from .scrap import get_rating
def book_list(request):
    books=Book.objects.all().order_by('year')
    pages=pagination(request,books,2)

    context={'items':pages[0],
          'page_range':pages[1]
    }

    return render(request,'books/book_list.html',context)

def book_detail(request,slug):
    #return HttpResponse(slug)
    book=Book.objects.get(slug=slug)
    rating=get_rating(book.isbn)
    comments='https://www.goodreads.com/api/reviews_widget_iframe?did=38607&format=html&header_text=Goodreads+reviews&isbn='+str(book.isbn)+'&links=660&min_rating=&num_reviews=&review_back=ffffff&stars=000000&stylesheet=&text=444'
    detail={
    'book':book,
    'rating':rating,
    'comments':comments

    }
    return render(request,'books/book_detail.html',detail)
