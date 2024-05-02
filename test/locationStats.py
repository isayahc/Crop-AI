import os
import googlemaps
import requests
from dotenv import load_dotenv
load_dotenv()

def get_coordinates(api_key, address):
    gmaps = googlemaps.Client(key=api_key)

    try:
        # Geocode the address
        geocode_result = gmaps.geocode(address)
        # Extract latitude and longitude
        if geocode_result:
            location = geocode_result[0]['geometry']['location']
            latitude = location['lat']
            longitude = location['lng']
            return latitude, longitude
        else:
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None
tempApiKey = os.environ.get('TEMP_API_KEY')
def get_temp(address) :
    coordinates = get_coordinates(os.environ.get('GMAPS_API_KEY'), address)
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={coordinates[0]}&lon={coordinates[1]}&appid={tempApiKey}'
    response = requests.get(url)
    data = response.text
    place = data.index('temp')
    first = int(place+6)
    last = int(place+12)
    return (float(data[first : last]) - 273)
def get_humidity(address) :
    coordinates = get_coordinates(os.environ.get('GMAPS_API_KEY'), address)
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={coordinates[0]}&lon={coordinates[1]}&appid={tempApiKey}'
    response = requests.get(url)
    data = response.text
    place = data.index('humidity')
    first = int(place+10)
    last = int(place+12)
    return (float(data[first : last]) )

    #print(data[first,last])
    #weatherStats = requests.post(url, data=data)
    #temp = weatherStats['temp'] 
    #return temp
