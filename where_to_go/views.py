from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404

from places.models import Location


def index(request):
    all_locations = Location.objects.all()

    locations_on_map = []

    for location in all_locations:
        location_properties = {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [location.lng, location.lat]
          },
          "properties": {
            "title": location.title,
            "placeId": location.title,
            "detailsUrl": ""
          }
        }

        locations_on_map.append(location_properties)


    data = {'places':
        {
        "type": "FeatureCollection",
        "features": locations_on_map,
        }
    }

    return render(request, "index.html", context=data)


def get_location(request, location_id):
    target_location = get_object_or_404(Location, id=location_id)

    location = {
        "title": target_location.title,
        "imgs": [image.photo.url for image in target_location.images.all()],
        "description_short": target_location.description_short,
        "description_long": target_location.description_long,
        "coordinates": {
          "lat": target_location.lat,
          "lng": target_location.lng
        }
    }

    return JsonResponse(location, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 2})
