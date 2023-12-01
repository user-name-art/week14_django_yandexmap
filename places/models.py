from django.db import models
from tinymce import models as tinymce_models


class Location(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description_short = models.TextField()
    description_long = tinymce_models.HTMLField()
    lat = models.FloatField(verbose_name='широта')
    lng = models.FloatField(verbose_name='долгота')

    def __str__(self):
        return self.title


class Image(models.Model):
    location = models.ForeignKey(Location, related_name='images', on_delete=models.CASCADE)
    photo = models.ImageField(null=True, blank=True)
    position = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ['position']

    def __str__(self):
        return f'{self.position} {self.location.title}'
