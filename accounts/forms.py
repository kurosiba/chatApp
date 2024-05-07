from django import forms
from .models import User

class RegistForm(forms.Form):
    name = forms.CharField(max_length=50)
    login_id = forms.CharField(max_length=50)
    passwd = forms.CharField(max_length=100)