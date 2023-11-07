from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

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
