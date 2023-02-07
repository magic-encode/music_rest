from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=150)
    picture = models.URLField(blank=True)



