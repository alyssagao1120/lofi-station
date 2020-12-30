from django.db import models
from pathlib import Path
from django.db.models.aggregates import Count
import random

# Create your models here.



class Song(models.Model):
    song_title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    file = models.FileField(upload_to="songs/")

    # toString() function
    def __str__(self):
        return f"'{self.song_title}' By: {self.artist}"

class Artwork(models.Model):
    title = models.CharField(max_length=500, default="Untitled")
    description = models.TextField()
    artist = models.CharField(max_length=500, default="Unknown")
    file = models.FileField()
    approved = models.BooleanField(default=False)

    # toString() function
    def __str__(self):
        return f"ARTWORK:'{self.title}' By: {self.artist}, APPROVED: {self.approved}"

    def randomArtwork(self):
        items = Artwork.objects.all().filter(approved=True)
        random_item = random.choice(items)
        # print('random item found was: ' + random_item.title)
        return random_item


