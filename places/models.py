from django.db import models
from tinymce import models as tinymce_models


class Location(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name='название')
    short_description = models.TextField(verbose_name='короткое описание', blank=True)
    long_description = tinymce_models.HTMLField(verbose_name='подробное описание', blank=True)
    lat = models.FloatField(verbose_name='широта')
    lng = models.FloatField(verbose_name='долгота')

    def __str__(self):
        return self.title


class Image(models.Model):
    location = models.ForeignKey(Location, related_name='images', verbose_name='место', on_delete=models.CASCADE)
    photo = models.ImageField(null=True, blank=True, verbose_name='изображение')
    position = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        verbose_name='позиция'
    )

    class Meta:
        ordering = ['position']

    def __str__(self):
        return f'{self.position} {self.location.title}'
