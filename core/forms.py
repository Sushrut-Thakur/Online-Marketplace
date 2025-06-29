from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={
		'placeholder': 'Enter username',
		'class': 'w-full px-2 py-2 rounded-xl',
	}))

	password = forms.CharField(widget=forms.PasswordInput(attrs={
		'placeholder': 'Enter password',
		'class': 'w-full px-2 py-2 rounded-xl',
	}))

class SignupForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')
	
	username = forms.CharField(widget=forms.TextInput(attrs={
		'placeholder': 'Enter username',
		'class': 'w-full px-2 py-2 rounded-xl',
	}))

	email = forms.EmailField(widget=forms.EmailInput(attrs={
		'placeholder': 'Enter email address',
		'class': 'w-full px-2 py-2 rounded-xl',
	}))

	password1 = forms.CharField(widget=forms.PasswordInput(attrs={
		'placeholder': 'Enter password',
		'class': 'w-full px-2 py-2 rounded-xl',
	}))

	password2 = forms.CharField(widget=forms.PasswordInput(attrs={
		'placeholder': 'Re-enter password',
		'class': 'w-full px-2 py-2 rounded-xl',
	}))