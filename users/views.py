from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import EditForm, LoginForm, SignUpForm

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(request.GET.get('next') or 'home')
            else:
                messages.error(request, "Username or Password is incorrect")
    else:
        form = LoginForm()
    return render(request, 'signup.html',{'form': form, 'action': 'Login'})

def logout_user(request):
    logout(request)
    return redirect(request.GET.get('next') or 'home')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect(request.GET.get('next') or 'home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form, 'action': 'Sign up'})

@login_required
def view_profile(request):
    return render(request, 'profile.html')

@login_required
def modify_profile(request):
    if(request.method == 'POST'):
        form = EditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditForm(instance=request.user)
    return render(request, 'signup.html', {'form': form, 'action': 'Modify User'})