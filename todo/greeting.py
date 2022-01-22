import datetime
import requests
import os
from suntime import Sun
from geopy.geocoders import Nominatim
import ipapi

def get_location():
    response = ipapi.location()
    return response['city']

def get_greeting_time(loc):

    now = datetime.datetime.now()

    # Nominatim API to get latitude and longitude
    geolocator = Nominatim(user_agent="todoDjango")

    try:
        place = loc
        print('place', place)
        current_location = geolocator.geocode(place)
        # latitude and longitude fetch
        latitude = current_location.latitude
        longitude = current_location.longitude
        sun = Sun(latitude, longitude)
    except:
        return 'Howdy'

    # sunset and sunrise config
    time_zone = datetime.date(now.year, now.month, now.day)
    sun_rise = sun.get_local_sunrise_time(time_zone)
    sun_dusk = sun.get_local_sunset_time(time_zone)

    # morning interval
    if now.hour >= sun_rise.hour and now.minute >= sun_rise.minute and now.hour < 12:
        return 'Good Morning'

    # afternoon interval
    if now.hour >= 12 and now.hour < sun_dusk.hour:
        return 'Good Afternoon'

    # evening interval
    if now.hour >= sun_dusk.hour and now.minute >= sun_dusk.minute:
        return 'Good Evening'