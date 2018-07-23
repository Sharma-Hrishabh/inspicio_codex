from django.conf.urls import url
from . import views

app_name='books'

urlpatterns = [
    url(r'^$',views.book_list,name="list"),
    url(r'^search/$',views.search,name="search"),
    url(r'^(?P<slug>[\w-]+)/$',views.book_detail,name="detail"),
    url(r'^search/(?P<slug>[\w-]+)/$',views.book_detail,name="detail"),
]
