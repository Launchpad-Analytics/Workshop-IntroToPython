import openmeteo_requests
import argparse
from geopy.geocoders import Nominatim


def get_city_latlong(city_name):
  # Convert a city name into latitude and longitude coordinates.
  geolocator = Nominatim(user_agent="my_city_geocoder")
  location = geolocator.geocode(city_name)
  if location:
    return [location.latitude, location.longitude]
  else:
    return None


def weather_lookup(coords):
  # Query the weather API for current and forecast temperatures.
  openmeteo = openmeteo_requests.Client()

  url = "https://api.open-meteo.com/v1/forecast"
  params = {
    "latitude": coords[0],
    "longitude": coords[1],
    "daily": ["temperature_2m_max", "temperature_2m_min"],
    "current": "temperature_2m",
    "timezone": "America/New_York",
    "temperature_unit": "fahrenheit",
  }

  responses = openmeteo.weather_api(url, params=params)

  current_temp = round(responses[0].Current().Variables(0).Value())
  max_temp = round(float(responses[0].Daily().Variables(0).ValuesAsNumpy().max()))
  min_temp = round(float(responses[0].Daily().Variables(1).ValuesAsNumpy().max()))

  return current_temp, max_temp, min_temp


def main():
  # Parse a city name from the command line and print weather results.
  parser = argparse.ArgumentParser()
  parser.add_argument('-c', '--city')
  args = parser.parse_args()

  city_coords = get_city_latlong(args.city)

  current_temp, max_temp, min_temp = weather_lookup(city_coords)
  print("Weather in: " + str(args.city) + " (" + str(city_coords) + ")")
  print("Current Temp: " + str(current_temp))
  print("Max Temp: " + str(max_temp))
  print("Min Temp: " + str(min_temp))


if __name__ == "__main__":
  main()
