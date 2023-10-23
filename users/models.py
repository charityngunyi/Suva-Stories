# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    about = models.CharField(max_length=450)