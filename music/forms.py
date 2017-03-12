from django.contrib.auth.models import User 
from django import forms 


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	email = forms.CharField()
	class Meta:
		model = User
		fields =  ['username','email','password']



class LoginForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)	
	class Meta:
		model = User
		fields =  ['username','password']