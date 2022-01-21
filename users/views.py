from base64 import urlsafe_b64decode
import email
from django.forms import models
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import EditForm, LoginForm, UserForm, PasswordResetForm, NewPasswordResetForm
from django.core.mail import send_mail
from . import models
from mysite import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string

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
    return render(request, 'login.html',{'form': form, 'action': 'Login'})

def logout_user(request):
    logout(request)
    return redirect(request.GET.get('next') or 'home')

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password1'] == form.cleaned_data['password2']:
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password1'])
                user.save()
                return redirect(request.GET.get('next') or 'home')
    else:
        form = UserForm()
    return render(request, 'form.html', {'form': form,  'action': 'Sign up'})

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
    return render(request, 'form.html', {'form': form, 'action': 'Modify User'})

def password_reset(request):
    if request.method == 'POST':
        form=PasswordResetForm(request.POST)
        if form.is_valid():
            user=models.Users.objects.filter(email=form.cleaned_data['email'])
            if user:
                subject = "Password Reset Requested"
                email_template_name = "new_password_email.txt"
                c={'protocol':request.scheme, 'domain':request.META['HTTP_HOST'], 'uid':urlsafe_base64_encode(force_bytes(user[0].pk)), 'token':default_token_generator.make_token(user[0])}
                message = render_to_string(email_template_name, c)
                send_mail(subject, message, settings.EMAIL_HOST_USER, [user[0].email], fail_silently=False)

                return redirect('/accounts/password_reset/done/')
            else:
                messages.error(request, "Email does not exist")
    else:
        form=PasswordResetForm()

    return render(request, 'form.html', {'form': form, 'action': 'Reset Password'})

def password_reset_confirm(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64)
        user = models.Users.objects.get(pk=uid)
        print(uid)
        print(user)
        print(default_token_generator.check_token(user, token))
    except(TypeError, ValueError, OverflowError, models.Users.DoesNotExist):
        user = None
    if user is not None:
        if request.method == 'POST':
            form = NewPasswordResetForm(request.POST)
            if form.is_valid():
                user.set_password(form.cleaned_data['password1'])
                user.save()
                return redirect('/accounts/login')
        else:
            form = NewPasswordResetForm()
        return render(request, 'form.html', {'form': form, 'action': 'Reset Password'})
    else:
        return HttpResponse("Link is invalid")

def password_reset_done(request):
    return render(request, 'passwordresetdone.html')