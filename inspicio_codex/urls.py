
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views

app_name="main"

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^accounts/',include('accounts.urls')),
    url(r'^books/',include('books.urls')),


    url(r'^$',views.home,name="home"),
    url(r'^about/$',views.about),


]
