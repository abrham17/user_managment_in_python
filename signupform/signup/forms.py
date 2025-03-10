from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'Placeholder': 'your username',
        'class': 'w-full mb-3 p-3 bg-gray-100 rounded-xl border-solid border-2 border-gray-200'
    }))
    
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'your email',
        'class': 'w-full mb-3 p-3 bg-gray-100 rounded-xl'
    }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'your password',
        'class': 'w-full mb-3 p-3 bg-gray-100 rounded-xl'
    }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'repeat your password',
        'class': 'w-full mb-3 p-3 bg-gray-100 rounded-xl'
    }))
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

