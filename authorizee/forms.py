from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.http import request

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class loginform(forms, forms.Form):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username= username, password=password)
    #if user is not None: