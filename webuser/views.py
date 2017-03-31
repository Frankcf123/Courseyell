from django.shortcuts import render, redirect
from .forms import SignUpForm,LoginForm
from .models import WebUser
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    # user = request.user
    return render(request, 'index.html')

def userRegister(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if not form.is_valid():
            return render(request,'register.html',{'form':form})
        else:
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password=form.cleaned_data.get('password')
            User.objects.create_user(username=username,password=password,email=email,
                                     )
            user = authenticate(username=username,password=password)
            webuser = WebUser(user=user)
            webuser.save()
            login(request,user)
            return redirect('/index')
    else:
        return render(request,'register.html',{'form':SignUpForm()})


def userLogin(request):
    if request.user.is_authenticated():
        return redirect('/index')
    if request.method=="POST":
        form = LoginForm(request.POST)
        # print form.is_valid()
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password= form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            login(request,user)
            return render(request,'index.html')
        else:
            return render(request,'login.html',{'form':form})
    else:
        return render(request,'login.html',{'form':LoginForm()})


def userLogout(request):
    logout(request)
    return redirect('/login')
