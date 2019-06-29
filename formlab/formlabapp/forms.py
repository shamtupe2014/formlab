from django import forms
from.models import *
from django.contrib.auth.models import User

class registration_form(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(),required=True,max_length=20)
    last_name = forms.CharField(widget=forms.TextInput(),required=True,max_length=20)
    birthday = forms.DateField(widget=forms.DateInput(),required=True)
    city = forms.CharField(widget=forms.TextInput(),required=True,max_length=20)
    email = forms.EmailField(required=True)
    phone = forms.IntegerField(widget=forms.NumberInput)

    class Meta():
        model = registration
        fields = ["first_name","last_name","birthday","city","phone","email"]


class userform(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholde':'Enter username'}),required=True,max_length=50)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholde': 'Enter first name'}),required=True, max_length=50)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholde': 'Enter last name'}),required=True, max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholde': 'Enter password'}),required=True, max_length=50)
    Confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholde': 'Confirm password'}), required=True,max_length=50)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholde': 'Enter email ID'}),required=True, max_length=50)

    class Meta():
        model = User
        fields = ['username','first_name','last_name','email','password']


