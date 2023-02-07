from django.db import models


class Song(models.Model):
    album = models.ForeignKey('music.Album', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=150)
    cover = models.URLField(blank=True)
    source = models.URLField()

    listened = models.PositiveIntegerField(default=0)
    

