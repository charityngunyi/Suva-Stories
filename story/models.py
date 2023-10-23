from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Genre(models.Model):
    # This class enables to create tender categories.
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    author = models.ForeignKey(get_user_model(), related_name='editors', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'genre'
        verbose_name_plural = 'genres'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('genre_detail', args=[str(self.id)])


class Story(models.Model):
    # class enables to edit the tenders.
    title = models.CharField(max_length=250)
    genre = models.ForeignKey(Genre, related_name='genres', on_delete=models.CASCADE)
    story = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='stories/%Y/%m/%d')
    # user = models.ForeignKey(User,related_name='owners', on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), related_name='stories', on_delete=models.CASCADE)


    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('story_detail', args=[str(self.id)])
