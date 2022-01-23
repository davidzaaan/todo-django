import datetime
from suntime import Sun
from geopy.geocoders import Nominatim
import ipapi
import requests

def get_location():
    ip = requests.get('https://api.ipify.org/').text # retrieving the ID
    response = ipapi.location(ip=ip, output='city')
    
    return response

def get_greeting_time(loc):

    now = datetime.datetime.now()

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
    

    # morning interval
    if (now.hour >= sun_rise.hour and now.minute >= sun_rise.minute) and now.hour < 12:
        return 'Good Morning'

    if now.hour > 12 and (now.hour < sun_dusk.hour and now.minute < sun_dusk.minute):
        return 'Good Afternoon'

    if (now.hour >= sun_dusk.hour and now.minute >= sun_dusk.minute) < sun_rise.hour:
        return 'Good Evening'