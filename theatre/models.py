from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    movie_title = models.CharField(max_length=250)
    thumbnail = models.FileField()
    clip = models.FileField()
    price = models.IntegerField()


class Coin(models.Model):
    user = models.CharField(max_length=100)
    spare_coin = models.IntegerField()


class UserMovie(models.Model):
    user = models.CharField(max_length=100)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
