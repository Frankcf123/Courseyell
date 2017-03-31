from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import WebUser
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    # user = request.user
    return render(request, 'index.html')

def register(request):
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
