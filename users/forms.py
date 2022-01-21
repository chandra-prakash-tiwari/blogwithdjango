from cProfile import label
from distutils.log import error
from django import forms
from django.contrib.auth.models import User
from users import models


class LoginForm(forms.ModelForm):
    class Meta:
        model = models.Authentication
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'autofocus': True, 'required': True}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        }



class EditForm(forms.ModelForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name', 'autofocus': True,}), required=False, label='First Name' )
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name', }), required=False, label='Last Name')
    username=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username',}), required=True, label='Username', help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.")
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', }), required=False, label='Email')
    phone=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile Number',}), required=False, label='Mobile Number')
    avatar=forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Profile Picture',}), required=False, label='Profile Picture')
    class Meta:
        model = models.Users 
        fields = [ 'first_name', 'last_name', 'username', 'email', 'avatar', 'phone' ]


class UserForm(forms.ModelForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name', 'autofocus': True,}), required=False, label='First Name' )
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name', }), required=False, label='Last Name')
    username=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username',}), required=True, label='Username', help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.")
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', }), required=False, label='Email')
    phone=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile Number',}), required=False, label='Mobile Number')
    avatar=forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Profile Picture',}), required=False, label='Profile Picture')
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', }), required=True, label='Password' ,help_text="")
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password',}), required=True, label='Confirm Password')

    class Meta:
        model = models.Users 
        fields = [ 'first_name', 'last_name', 'username', 'email', 'avatar', 'phone' , 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username == '':
            raise forms.ValidationError('This field is required.')
        return username

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if password1 == '':
            raise forms.ValidationError('This field is required.')
        return password1

    def clean_password2(self):
        error=[]
        password2 = self.cleaned_data.get('password2')
        password1 = self.cleaned_data.get('password1')
        if len(password2) < 8:
            error.append('Password must be at least 8 characters long.')
        if not any(char.isdigit() for char in password2):
            error.append('Password must contain at least one number.')
        if not any(char.isupper() for char in password2):
            error.append('Password must contain at least one uppercase letter.')
        if not any(char.islower() for char in password2):
            error.append('Password must contain at least one lowercase letter.')
        if password1 != password2:
            error.append('Passwords do not match.')
        if error:
            raise forms.ValidationError(error)
        return password2


class PasswordResetForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', }), required=True, label='Email')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email == '':
            raise forms.ValidationError('This field is required.')
        return email


class NewPasswordResetForm(forms.Form):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', }), required=True, label='Password' ,help_text="")
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password',}), required=True, label='Confirm Password')

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if password1 == '':
            raise forms.ValidationError('This field is required.')
        return password1

    def clean_password2(self):
        error=[]
        password2 = self.cleaned_data.get('password2')
        password1 = self.cleaned_data.get('password1')
        if len(password2) < 8:
            error.append('Password must be at least 8 characters long.')
        if not any(char.isdigit() for char in password2):
            error.append('Password must contain at least one number.')
        if not any(char.isupper() for char in password2):
            error.append('Password must contain at least one uppercase letter.')
        if not any(char.islower() for char in password2):
            error.append('Password must contain at least one lowercase letter.')
        if password1 != password2:
            error.append('Passwords do not match.')
        if error:
            raise forms.ValidationError(error)
        return password2
