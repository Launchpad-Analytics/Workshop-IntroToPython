from datetime import datetime
import json
from zoneinfo import ZoneInfo
import time
from s310.day2.get_weather_info import get_city_latlong, weather_lookup


def greeting(name):
  # Build and return the personalized greeting message.
  greeting_message = f"Good Morning, {name}!"
  return greeting_message


def time_and_date(timezone):
  # Get the current date and time for the selected timezone.
  now_ny = datetime.now(ZoneInfo(timezone))
  today = f"Today is {now_ny.strftime('%A, %B %d, %Y')}"
  current_time = f"The time is {now_ny.strftime('%I:%M %p')}"

  return [today, current_time]


def get_weather(location):
  # Use the weather helper functions to create a weather update message.
  city_coords = get_city_latlong(location)
  current_temp, max_temp, min_temp = weather_lookup(city_coords)
  weather_message = f"The current temperature in {location} is {current_temp} with a high of {max_temp} and a low of {min_temp}"
  return weather_message


def get_headlines():
  # Read the saved headlines from a text file and clean each line.
  with open('headlines.txt', 'r') as file:
    headlines = file.readlines()

  return [headline.strip() for headline in headlines]


def main():
  # Load user settings and build the full wake-up message list.
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