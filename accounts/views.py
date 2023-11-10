from django.shortcuts import render, redirect
from .models import User
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

def follows(request, username):
    me = request.user
    you = User.objects.get(username=username)

    # 이미 팔로잉이 되어있는경우
    if you in me.followings.all():
        me.followings.remove(you)   
    # 팔로잉이 되어있지 않은 경우
    else:
        me.followings.add(you)
    return redirect('accounts:profile', username=username)