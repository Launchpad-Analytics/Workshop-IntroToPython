# def greeting(name):
#   print(f"Good Morning, {name}!")

# greeting("Kelly")

# from datetime import datetime
# from zoneinfo import ZoneInfo
# import time

# def greeting(name):
#   print(f"Good Morning, {name}!")
#   time.sleep(2)

#   now_ny = datetime.now(ZoneInfo("America/New_York"))

#   print(f"Today is {now_ny.strftime('%A, %B %d, %Y')}")
#   time.sleep(2)

#   print(f"The time is {now_ny.strftime('%I:%M %p')}")
#   time.sleep(2)

# greeting("Kelly")



# from datetime import datetime
# from zoneinfo import ZoneInfo
# import time

# def greeting(name):

#   greeting = f"Good Morning, {name}!"

#   now_ny = datetime.now(ZoneInfo("America/New_York"))
#   today = f"Today is {now_ny.strftime('%A, %B %d, %Y')}"
#   current_time = f"The time is {now_ny.strftime('%I:%M %p')}"

#   print(greeting)
#   time.sleep(1)
#   print(today)
#   time.sleep(1)
#   print(current_time)


# greeting("Kelly")



# from datetime import datetime
# from zoneinfo import ZoneInfo
# import time

# def greeting(name):

#   greeting = f"Good Morning, {name}!"

#   now_ny = datetime.now(ZoneInfo("America/New_York"))
#   today = f"Today is {now_ny.strftime('%A, %B %d, %Y')}"
#   current_time = f"The time is {now_ny.strftime('%I:%M %p')}"

#   messages = [greeting, today, current_time]
#   for m in messages:
#     time.sleep(2)
#     print(m)


# greeting("Kelly")



# from datetime import datetime
# from zoneinfo import ZoneInfo
# import time

# def greeting(name):

#   greeting = f"Good Morning, {name}!"

#   now_ny = datetime.now(ZoneInfo("America/New_York"))
#   today = f"Today is {now_ny.strftime('%A, %B %d, %Y')}"
#   current_time = f"The time is {now_ny.strftime('%I:%M %p')}"

#   messages = [greeting, today, current_time]

#   return messages


# display_messages = greeting("Kelly")
# # print(display_messages[1])
# for m in display_messages:
#   time.sleep(2)
#   print(m)





# from datetime import datetime
# from zoneinfo import ZoneInfo
# import time

# name = "Kelly"

# def greeting(name):
#   greeting_message = f"Good Morning, {name}!"
#   return greeting_message

# def time_and_date(time_zone):
#   now_ny = datetime.now(ZoneInfo(time_zone))
#   today = f"Today is {now_ny.strftime('%A, %B %d, %Y')}"
#   current_time = f"The time is {now_ny.strftime('%I:%M %p')}"
#   return [today, current_time]

# def get_weather(location):
#   weather_info = None
#   weather_message = f"The current temperature in {location} is {None} with a high of {None} and a low of {None}"
#   return weather_message

# def main():
#   messages = []
#   messages.append(greeting(name))
#   # messages.append(time_and_date("America/New_York"))
#   messages += time_and_date("America/New_York")
#   messages.append(get_weather("Pittsburgh"))

#   for m in messages:
#     time.sleep(1)
#     print(m)


# main()

# from datetime import datetime
# from zoneinfo import ZoneInfo
# import time

# name = "Kelly"

# def greeting(name):
#   greeting_message = f"Good Morning, {name}!"
#   return greeting_message

# def time_and_date(time_zone):
#   now_ny = datetime.now(ZoneInfo(time_zone))
#   today = f"Today is {now_ny.strftime('%A, %B %d, %Y')}"
#   current_time = f"The time is {now_ny.strftime('%I:%M %p')}"
#   return [today, current_time]

# def get_weather(location):
#   weather_info = None
#   weather_message = f"The current temperature in {location} is {None} with a high of {None} and a low of {None}"
#   return weather_message

# def get_headlines():
#   with open('headlines.txt', 'r') as file:
#     headlines = file.readlines()
  
#   return [headline.strip() for headline in headlines]

# def main():
#   message_list = []
#   message_list.append(greeting(name))
#   # message_list.append(time_and_date("America/New_York"))
#   message_list += time_and_date("America/New_York")
#   message_list.append(get_weather("Pittsburgh"))
#   message_list.append("Here are today's headlines:")
#   message_list += get_headlines()
#   message_list.append("Have a great day!")

#   for m in message_list:
#     time.sleep(1)
#     print(m)


# main()


from datetime import datetime
from zoneinfo import ZoneInfo
import time
from get_weather_info import weather_lookup

name = "Kelly"

def greeting(name):
  greeting_message = f"Good Morning, {name}!"
  return greeting_message

def time_and_date(time_zone):
  now_ny = datetime.now(ZoneInfo(time_zone))
  today = f"Today is {now_ny.strftime('%A, %B %d, %Y')}"
  current_time = f"The time is {now_ny.strftime('%I:%M %p')}"
  return [today, current_time]

def get_weather(location):
  pit_coords = [40.44, -79.9959]
  current_temp, max_temp, min_temp = weather_lookup([40.44, -79.9959])
  weather_message = f"The current temperature in {location} is {current_temp} degrees, with a high of {max_temp} and a low of {min_temp}"
  return weather_message

def get_headlines():
  with open('headlines.txt', 'r') as file:
    headlines = file.readlines()
  
  return [headline.strip() for headline in headlines]

def main():
  message_list = []
  message_list.append(greeting(name))
  # message_list.append(time_and_date("America/New_York"))
  message_list += time_and_date("America/New_York")
  message_list.append(get_weather("Pittsburgh"))
  message_list.append("Here are today's headlines:")
  message_list += get_headlines()
  message_list.append("Have a great day!")

  for m in message_list:
    time.sleep(1)
    print(m)


if __name__ == "__main__":
  main()


# from good_morning import get_headlines
# import cowsay

# for h in get_headlines():
#   cowsay.cow(h)