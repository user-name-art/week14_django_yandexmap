from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Location


def index(request):
    locations = Location.objects.all()

    locations_on_map = [
        {
          'type': 'Feature',
          'geometry': {
            'type': 'Point',
            'coordinates': [location.lng, location.lat]
          },
          'properties': {
            'title': location.title,
            'placeId': location.title,
            'detailsUrl': reverse('get-location', kwargs={'location_id': location.id})
          }
        }
        for location in locations
    ]

    data = {
        'places': {
            'type': 'FeatureCollection', 'features': locations_on_map
        }
    }

    return render(request, 'index.html', context=data)


def get_location(request, location_id):
    target_location = get_object_or_404(Location.objects.prefetch_related('images'), id=location_id)

    location = {
        'title': target_location.title,
        'imgs': [image.photo.url for image in target_location.images.all()],
        'short_description': target_location.short_description,
        'long_description': target_location.long_description,
        'coordinates': {
          'lat': target_location.lat,
          'lng': target_location.lng
        }
    }

    return JsonResponse(location, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 2})
