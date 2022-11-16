from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    fb_link = models.URLField(max_length=255)
    yt_link = models.URLField(max_length=255, blank=True)
    insta_link = models.URLField(max_length=255)
    photo = models.ImageField(upload_to='media/team/%Y')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class Slider(models.Model):
    headline = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    button_text = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/slider/%Y')
    created_date = models.DateTimeField(auto_now_add=True)
    url = models.URLField(max_length=255, blank=True)

    def __str__(self):
        return self.headline
