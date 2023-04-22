from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Anime(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.title


class Popular(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

class Action(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

class Family(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

class Kids(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

class Video(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title