import datetime
from suntime import Sun
from geopy.geocoders import Nominatim
import ipapi
import requests

def get_location():
    ip = requests.get('https://api.ipify.org/').text # retrieving the IP
    response = ipapi.location(ip=ip, output='city') # city name to locate
    
    return response

def get_greeting_time(loc):

    now = datetime.datetime.now() # current time

    # Nominatim API to get latitude and longitude
    geolocator = Nominatim(user_agent="todoDjango")

    try:
        place = loc
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

    
    if now.hour >= sun_rise.hour:
        # morning interval
        if now.hour < 12:
            return 'Good Morning'
        elif now.hour < sun_dusk.hour:
            # afternoon interval
            return 'Good Afternoon'
        else:
            # night interval
            return 'Good Evening'
    else:
        # night
        return 'Good Evening'

    