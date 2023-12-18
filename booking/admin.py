from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
#from .forms import RegistrationForm, UserProfileForm


class UserProfileInline(admin.StackedInline):
  model = UserProfile
  can_delete = False
  verbose_name_plural = 'User Profile'
  
class CustomUserAdmin(UserAdmin):
  inlines = (UserProfileInline, )

admin.site.unregister(User)

admin.site.register(User, CustomUserAdmin)
