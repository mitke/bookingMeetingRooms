from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


class RegistrationForm(UserCreationForm):
 
  class Meta:
    model = User
    fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']

class UserProfileForm(forms.ModelForm):
  telephone_number = forms.CharField(max_length=100, required=True)
  medical_title = forms.CharField(max_length=100, required=False)
  
  class Meta:
    model = UserProfile
    fields = ['telephone_number', 'medical_title']