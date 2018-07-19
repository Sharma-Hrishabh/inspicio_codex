from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.http import HttpResponse


def signup_view(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return HttpResponse('loginned after signup')
    else:
        user = request.user
        profile = user.profile
        form = UserCreationForm(instance=profile)
    return render(request,'accounts/signup.html',{'form':form})



def login_view(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return HttpResponse('loginned')
    else:
        form = AuthenticationForm
    return render(request,'accounts/login.html',{'form':form})
