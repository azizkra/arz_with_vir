from django import forms
from .models import NewUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from .models import NewUser, Profile

class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = NewUser
        fields = ('email', 'username', 'password1', 'password2')
        
        widgets = {
            'email':forms.TextInput(attrs={'class': 'form-control'}),
            'username':forms.TextInput(attrs={'class': 'form-control'}),
        }
        
        
        
class UserLoginForm(forms.Form):
    email = forms.CharField(label='username', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    


class UserUpdateForm(forms.ModelForm):
    #email = forms.EmailField()
    
    class Meta:
        model = NewUser
        fields = ["username",]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields= ['image']
        