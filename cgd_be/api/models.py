from django.db import models

# Create your models here.

class Word(models.Model):
    word = models.CharField(max_length=50)
    definition = models.TextField()
    usage = models.TextField()
    origin = models.CharField(max_length=50)

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
