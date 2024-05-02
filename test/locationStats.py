import googlemaps

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
