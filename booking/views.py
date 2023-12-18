from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import RegistrationForm, UserProfileForm

def home(request):
  return render(request, 'booking/home.html')


def register(request):
  if request.method == 'POST':
    user_form = RegistrationForm(request.POST)
    profile_form = UserProfileForm(request.POST)
    if user_form.is_valid() and profile_form.is_valid():
      user = user_form.save()
      profile = profile_form.save(commit=False)
      profile.user = user
      profile.save()
      login(request, user)
      return redirect('home')
  else:
    user_form = RegistrationForm()
    profile_form = UserProfileForm()
  return render(request, 'registration/register.html', {'user_form': user_form, 'profile_form': profile_form})


def user_login(request):
  if request.method == 'POST':
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      user = form.get_user()
      login(request, user)
      return redirect('home')
  else:
    form = AuthenticationForm()
  return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
  logout(request)
  return redirect('home')
