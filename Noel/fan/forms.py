from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from django.forms import ModelForm
class Userfile(ModelForm):
    class Meta:
         model = UserProfile
         fields = ["nike_name", "desc", "sign", "birthday", "address", "img"]