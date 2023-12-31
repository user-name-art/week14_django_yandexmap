from urllib.parse import urlsplit

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Image, Location


def save_image_to_db(photo_url, location, content):
    filename = str(urlsplit(photo_url).path).split('/')[-1]
    Image.objects.create(
        location=location,
        photo=ContentFile(content, name=filename)
    )


class Command(BaseCommand):
    help = 'Download new locations'

    def add_arguments(self, parser):
        parser.add_argument('url', nargs='+', type=str)

    def handle(self, *args, **options):
        response = requests.get(options['url'][0])
        response.raise_for_status()
        place = response.json()

        location, created = Location.objects.get_or_create(
            title=place['title'],
            defaults={
                    'short_description': place['description_short'],
                    'long_description': place['description_long'],
                    'lat': place['coordinates']['lat'],
                    'lng': place['coordinates']['lng'],
            }

        )

        if not location.images.all():
            for photo_url in place['imgs']:
                response = requests.get(photo_url)
                response.raise_for_status()

                save_image_to_db(photo_url, location, response.content)

        self.stdout.write(self.style.SUCCESS('Successfully added location "%s"' % location.title))
