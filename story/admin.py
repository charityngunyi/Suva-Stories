# articles/admin.py
from django.contrib import admin
from .models import Story, Genre
admin.site.register(Story)
admin.site.register(Genre)