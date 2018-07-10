from django.conf.urls import url
from . import views

app_name='books'

urlpatterns = [
    url(r'^$',views.book_list,name="list"),
    url(r'^(?P<slug>[\w-]+)/$',views.book_detail,name="detail"),
]
