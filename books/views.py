from django.shortcuts import render,redirect
from .models import Book
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from books.config import pagination

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
    return render(request,'books/book_detail.html',{'book':book })
