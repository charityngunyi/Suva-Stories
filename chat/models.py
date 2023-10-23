# articles/models.py
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Message(models.Model):
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ('date',)
    
    def __str__(self):
        return self.message
    def get_absolute_url(self):
        return reverse('message_detail', args=[str(self.id)])