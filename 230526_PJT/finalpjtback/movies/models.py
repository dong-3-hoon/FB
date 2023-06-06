from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
# Create your models here.
class Movie(models.Model):
    adult = models.BooleanField(default=False)
    backdrop_path = models.TextField(blank=True)
    genre_ids = models.ManyToManyField(Genre)
    id = models.IntegerField(primary_key=True)
    original_language = models.CharField(max_length=30)
    original_title = models.TextField()
    overview = models.TextField(blank=True)
    popularity = models.FloatField(blank=True)
    poster_path = models.TextField(blank=True)
    release_date = models.DateField()
    title = models.TextField()
    video = models.BooleanField(default=False)
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    video_key = models.TextField()



class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    updated = models.BooleanField(default=False)
    content = models.TextField()
    created_at = models.CharField(max_length=20)
    
