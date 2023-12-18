from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  telephone_number = models.CharField(max_length=15, blank=True, null=True)
  medical_title = models.CharField(max_length=100, blank=True, null=True)

  def __str__(self):
    return self.user.username
