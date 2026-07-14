from datetime import datetime
import json
from zoneinfo import ZoneInfo
import time
from get_weather_info import get_city_latlong, weather_lookup


def greeting(name):
  greeting_message = f"Good Morning, {name}!"
  return greeting_message


def time_and_date(timezone):
  now_ny = datetime.now(ZoneInfo(timezone))
  today = f"Today is {now_ny.strftime('%A, %B %d, %Y')}"
  current_time = f"The time is {now_ny.strftime('%I:%M %p')}"

  return [today, current_time]

def get_weather(location):
  city_coords = get_city_latlong(location)
  # weather_info = None
  current_temp, max_temp, min_temp = weather_lookup(city_coords)
  weather_message = f"The current temperature in {location} is {current_temp} with a high of {max_temp} and a low of {min_temp}"
  return weather_message

def get_headlines():
  with open('headlines.txt', 'r') as file:
    headlines = file.readlines()
  
  return [headline.strip() for headline in headlines]

def main():
  with open("user_settings.json", "r") as file:
    user_settings = json.load(file)

  message_list = []
  message_list.append(greeting(user_settings["user_name"]))
  message_list += time_and_date(user_settings["user_time_zone"])
  message_list.append(get_weather(user_settings["user_location"]))
  message_list.append("Here are today's headlines:")
  message_list += get_headlines()
  message_list.append("Have a great day!")

  for m in message_list:
    time.sleep(1)
    print(m)


if __name__ == "__main__":
  main()