from django.shortcuts import render, redirect
from .forms import UserLoginForm , UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username = username , password = password)
            if user is not None:
                login(request,user)
                messages.success(request,'you logged in successfully!', 'success')
                return redirect('blog:all_articles')
            else:
                messages.error(request,'Wrong user name or password!', 'warning')
    else:
        form = UserLoginForm()
    return render(request,'accounts/login.html',{'form':form})


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'],cd ['email'],cd ['password1'])
            messages.success(request,'You are registered successfully! log in now!','success')
            return redirect('accounts:user_login')

    else:
        form = UserRegistrationForm()
    return render (request,'accounts/register.html', {'form':form})


def user_logout(request):
    logout(request)
    messages.success(request,'you logout successfully!','success')
    return redirect('blog:all_articles')
    
