from django.shortcuts import render, redirect
from .models import User
from posts.models import Post
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:index')

    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts_form.html', context)

def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())

            return redirect('posts:index')

    else:
        form = CustomAuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts_form.html', context)
    
def logout(request):
    auth_logout(request)
    return redirect('accounts:login')

def profile(request, username):
    user_info = User.objects.get(username=username)
    context = {
        'user_info': user_info,
    }
    return render(request, 'profile.html', context)
    