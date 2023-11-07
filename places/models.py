from django.db import models


class Location(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.TextField()
    description_long = models.TextField()
    lat = models.FloatField(verbose_name='широта')
    lng = models.FloatField(verbose_name='долгота')

    def __str__(self):
        return self.title
