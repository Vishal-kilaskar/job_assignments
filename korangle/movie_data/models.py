from django.db import models
from datetime import date


class Movies(models.Model):
    movie_title = models.CharField(max_length=100)
    movie_release_date = models.DateField(default=date)
    movie_upvotes = models.IntegerField(default=0)

