# Functions, Files, and Scripts

In this module, we're going to learn how to take the Python syntax we learned and give it legs.

# Session Setup
During this session, we're going to utilize more of the features in our Google Colab environment. If you utilized colab for the first session's notebook, you can keep that same notebook active. If not, you can start a new Colab session by following this link*: [New Notebook](colab.new)

(**Alternatively, if you chose to set up your local Python coding environment, you can follow along with your local environment. If you're not working with a linux system, then some of the command line inscructions may be different*)

We won't actually need the notebook for most of this session (you can still use it for scratchwork), so we're going to configure our view by opening a Terminal tab and extending it so that it takes up most of our screen. The Terminal button can be found in the bottom-left corner of the screen:

<img width="1916" height="952" alt="image" src="https://github.com/user-attachments/assets/31818590-0984-4eba-8a0b-d75cef8d78fc" />


When you're done, your Colab window might look something like this:
<img width="1918" height="944" alt="20260711-0252-35 7921598" src="https://github.com/user-attachments/assets/af2a705c-5b6c-48ab-a9c8-e539975d7113" />

## What is a terminal? Quick command line demo
A terminal is a text-based user interface that allows a user to access a computer system's resources... (TODO: FINISH EXPLANATION)

Here are some basic bash commands that you can run from the command line:

### Where am I? Use `pwd` to print your "working directory", or what folder you're currently inside of
<img width="314" height="164" alt="image" src="https://github.com/user-attachments/assets/7413f45b-a8d7-4c31-9658-3875cb731d8c" />

We are currently inside the `/content` folder, which is the default folder for the Colab environment.

### What's in here? Use `ls` to list all of the files in the current directory
<img width="280" height="150" alt="image" src="https://github.com/user-attachments/assets/97899847-34df-4ca6-b06f-45233aad4216" />

Running `ls` from the `content/` directory tells us that the only thing inside of our current working directory is another directory called `sample_data/`. To quicky see what's inside of this nested directory, we can pass it to the ls command like this:

`ls sample_data/`

This lists all of the files in this lower directory without having to navigate to it:
<img width="1074" height="188" alt="image" src="https://github.com/user-attachments/assets/290c6d29-de69-43ed-b2db-a5c2e798c9de" />

This `sample_data/` folder contains some popular practice datasets for machine learning, which Colab has included in the standard environment.

Similarly, we can also list the files that are in a higher level directory than our current working directory by using `ls ..`

<img width="910" height="212" alt="image" src="https://github.com/user-attachments/assets/17d60280-d33d-4349-9270-34319c73fb57" />

## Download the practice files by cloning the workshop repo

# Creating our first script:
In this context, a script is a file that houses a series of Python commands to be carried out in a sequential order... (TODO: Finish intro)

Using our same terminal window, we're going to create an empty python file with the following command:

```bash
touch good_morning.py
```

After a rief moment, your new python file should appear in the files list on the left. Double-click the script file to open it in a new tab. The terminal tab will be hidden by this new file, but you can drag it down below the script file to split the window if it suits your preference:

<img width="1916" height="938" alt="image" src="https://github.com/user-attachments/assets/d79e2f57-fe6b-482a-9f42-5a5eb826e338" />

To start, we're going to create as basic of a script as we can. We're going to create a single string variable `name`, and then print a custom greeting message using whatever name is passed to that variable:

```python title
# good_morning.py

name = "Kelly"

print("Good Morning, " + name + "!")
```
Next, we're going to run our script by running this command in our terminal:

```
python good_morning.py
```

After running, out output should look like this:

<img width="362" height="142" alt="image" src="https://github.com/user-attachments/assets/d9d9a82b-94f8-407e-a989-726c0bfc59d0" />

There's often many different ways to achieve the same result in programming, and each method may be better suited for what you want to accomplish. The concatenating of the text strings to build our message works well, but we can also use what's called an **f-string** to create better string templates and embed values directly. We're going to do that now with our print statement:

```python
name = "Kelly"

print(f"Good Morning, {name}!")
```

# Example Build: Personal Assistant Wake-up Message
<img width="60%" height="30%" alt="image" src="https://github.com/user-attachments/assets/89cf51de-70bd-4a78-858f-db74ea7deb64" />

> In this scenario, we're programming the software for a personal home tech product: a digital panel that displays weather information, news, and other customizable widgets to be displayed at a glance. The feature we'll be coding is the "Wake-up Routine", which plays after the user's morning alarm goas off and gives them the day's weather and news headlines.

## Adding the first function: customizing the greeting message

Using the same `good_morning.py` file, our first function will be to customize the greeting message based on the name of the user. The function will be called `greeting()`, and it will name the users name as it's 1 argument:

```python
name = "Kelly"

def greeting(user_name):
  print(f"Good Morning, {user_name}!")

greeting(name)
```
***Remember: after you create a function, you must call that function in your script in order for the code to run***

Save your script, and run in again from the terminal to verify that the greeting message still displays. You will repeat this process after every new element you add to your script:

```bash
python good_morning.py
```

## Using the built-in `datetime` module to display the current date time
The next step for our wake-up routine is to give the user the date and the current time, like this:

```
Good Morning, Kelly!
Today is Wednesday, July 29th
The time is 8:34 AM
```

In order to get the current date and time, we will use the `datetime` module, which is a **built-in** module of code that comes included with Python and contains several functions for achieving more complex tasks. In order to use those functions in our script, we first need to use an `import` statement to include the `datetime` module in our code. We will also need another module `zoneinfo` to get infromation about our specific timezone:

```python
from datetime import datetime
from zoneinfo import ZoneInfo
```

### What is a datetime?
TODO

### Using `strftime` to format the date and time

Using the `datetime.now()` function, we're going to grab the current datetime (using NYC as our location reference) and save it to a variable called `now_ny`:

`now_ny = datetime.now(ZoneInfo("America/New_York"))`

Because `now_ny` is a variable of type `datetime`, it now has all of the methods included in the `datetime` module. One of those methods is the `.strftime()` method, which formats the datetime into a string based on a custom-defined format. The format we want our date to be in is `[Weekday], [Month] [Day], [Year]`, so the format template we're going to pass to `.strftime()` is `'%A, %B %d, %Y'`:

```python
today = f"Today is {now_ny.strftime('%A, %B %d, %Y')}"
```

You don't need to memorize what each format code means, as you will often just look up the information when you're formatting datetimes for a specific task. [This post](https://www.programiz.com/python-programming/datetime/strftime) is an example resource you can use to loookup the right format codes you need. We'll use the same method to create a variable `current_time` with the time, and then add both statements to the greeting message.


> script checkpoint: `good_morning.py`
```python
from datetime import datetime
from zoneinfo import ZoneInfo
import time

def greeting(name):

  greeting = f"Good Morning, {name}!"

  now_ny = datetime.now(ZoneInfo("America/New_York"))
  today = f"Today is {now_ny.strftime('%A, %B %d, %Y')}"
  current_time = f"The time is {now_ny.strftime('%I:%M %p')}"

  print(greeting)
  time.sleep(1)
  print(today)
  time.sleep(1)
  print(current_time)


greeting("Kelly")
```
***Run the `good_morning.py` script in your terminal to verify that the script works***

We've also added the `time.sleep()` function to the script to give the output the appearance of a more natural delay.

## Code Improvement: Using lists and loops to optimize our code.
Notice the repeated `print()` and `time.sleep()` function calls? While it's manageable for the short list of 3 messages we have currently, it will quickly become slow and inefficient once the number of messages start to grow. A more efficient way to code this functionality is to create a list of all of the messages we want to send, and then create a **for loop** to print each message to the console:

```python
messages = [greeting, today, current_time]
  for m in messages:
    time.sleep(2)
    print(m)

greeting("Kelly")
```

## Code Improvement: Returning values instead of printing them
So far, we've been printing our messages to the console, which we've been using to act as our display screen as we test our code. The problem is that these test statements aren't allowing us to do anything with this data, like pass it off to the hardware component that would be displaying these messages on the product screen. So, the first major functionality improvement we're going to make to this script is to return a list containing our greeting, date, and time messages from the `greeting()` function instead of printing them to the console. 

Now that our `greeting()` function gives us access to the messages as data, we will use the function to generate a list of messages in a variable called `message_list` and implement the similar logic:

> script checkpoint: `good_morning.py`
```python
from datetime import datetime
from zoneinfo import ZoneInfo
import time

def greeting(name):

  greeting = f"Good Morning, {name}!"

  now_ny = datetime.now(ZoneInfo("America/New_York"))
  today = f"Today is {now_ny.strftime('%A, %B %d, %Y')}"
  current_time = f"The time is {now_ny.strftime('%I:%M %p')}"

  messages = [greeting, today, current_time]
  return messages


message_list = greeting("Kelly")

for m in message_list:
    time.sleep(2)
    print(m)
```

## Code Improvement: One Task Per Function

We've expanded our initial `greeting` function to also include information about time and date, but what if we just wanted the simple greeting by itself? With this function, we would have to parse out the greeting from the rest of the date and time information, which would quickly show us why it would be better to have a separate function for each logical piece of information.

We're going to keep the greeting message in the `greeting()` function, but move the time and date messages to a new function called `time_and_date()` that returns the `today` and `current_time` variables:

```python
def greeting(name):
  greeting_message = f"Good Morning, {name}!"
  return greeting_message

def time_and_date(time_zone):
  now_ny = datetime.now(ZoneInfo(time_zone))
  today = f"Today is {now_ny.strftime('%A, %B %d, %Y')}"
  current_time = f"The time is {now_ny.strftime('%I:%M %p')}"
  return [today, current_time]
```

## Adding Weather and News Message Functions
Copy the following two functions and add them to your script under the `time_and_date()` function 

```python
def get_weather(location):
  weather_info = None
  weather_message = f"The current temperature in {location} is {None} with a high of {None} and a low of {None}"
  return weather_message

def get_headlines():
  with open('headlines.txt', 'r') as file:
    headlines = file.readlines()
  
  return [headline.strip() for headline in headlines]
```

We're going to tackle the weather information last, so for now we'll make a skeleton function that returns the message template we want for our wake-up routine. This function will take a location as an argument, and return the current tempurature and forecasted high/low temperature forcast for the day in that location.

### Context Managers
The second function, `get_headlines()`, reads in a series of news headlines (listed in `headlines.txt`) and returns them as a list. The `with` statement you see in this function is called a **context manager**, which is used to efficiently handle memory and resources within Python when interacting with external files.  The `'r'` argument being passed designated that the text file is being opened in "read mode", which means that no changes can be made to the text in the file itself. Within this code block, the list variable `headlines` is being created by reading each line of text and passing in to a list created by the `.readlines()` method.

### List Comprehensions
Before we explain what's heppening in this `return` statement, copy the `with` block and paste it into a blank cell in your notebook. Then, call the `headlines` variable and oobserve the output. It should look something like this:

```
['Local Park Welcomes Record-Breaking Number of Geese after Implementing Mandatory Soft-Rock Playlist\n',
 'City Council Approves $4.2M Budget Hike to Upgrade Potholes with Eco-Friendly, Biodegradable Memory Foam\n',
 "Commuters Report Smoother Transit Experience Following Subway System’s Transition to 'Honor System' High-Fives\n",
 "Nationwide Coffee Chain Introducing 'Deconstructed Espresso' Served via Dropper Directly onto Tongue\n",
 'Regional Airport Flight Delays Plummet 40% after Replacing Boarding Queue with Mildly Competitive Musical Chairs']
```

When reading in the text file, the code is picking up the invisible newline (part of a category of **whitespace characters**) characters (`\n`) at the end of each line. We don't want these characters to mistakenly be read by the wake-up routine, so we need to programmatically loop through each list item and remove these characters. A function with this looping and cleaning logic fully written out might look like this:

```python
def get_headlines():
  with open('headlines.txt', 'r') as file:
    headlines = file.readlines()
  
  headlines_clean = []
  for line in headlines:
    line_clean = line.strip()
    headlines_clean.append(line_clean)
  
  return headlines_clean
```

In this function, the code makes it easy to read exactly what's happening to clean each line of text, but the last  5 lines of this function can also be collapsed into a single line of code by using a powerful tool called a **list comprehension**:

`return [headline.strip() for headline in headlines]`

### Discussion: Code Readability vs. Efficiency
TODO

## Code Improvement: Message List

You should now have 4 separate functions that are returning specific pieces of information needed to build the wake-up routine message. Keeping our same `message_list` variable and looping code that's at the bottom of our script, we're going to set `message_list` equal to an empty list, which we will use to add our messages to from all of our functions, along with some custom messages that we'll add to fill in the wake-up routine:

```python
name = "Kelly"
message_list = []
message_list.append(greeting(name))
message_list += time_and_date("America/New_York")
message_list.append(get_weather("Pittsburgh"))
message_list.append("Here are today's headlines:")
message_list += get_headlines()
message_list.append("Have a great day!")

for m in message_list:
  time.sleep(1)
  print(m)
```

> code checkpoint: `good_morning.py`
```python
from datetime import datetime
from zoneinfo import ZoneInfo
import time

def greeting(name):
  greeting_message = f"Good Morning, {name}!"
  return greeting_message


def time_and_date(timezone):
  now_ny = datetime.now(ZoneInfo(timezone))
  today = f"Today is {now_ny.strftime('%A, %B %d, %Y')}"
  current_time = f"The time is {now_ny.strftime('%I:%M %p')}"

  return [today, current_time]

def get_weather(location):
  weather_info = None
  weather_message = f"The current temperature in {location} is {None} with a high of {None} and a low of {None}"
  return weather_message

def get_headlines():
  with open('headlines.txt', 'r') as file:
    headlines = file.readlines()
  
  return [headline.strip() for headline in headlines]

name = "Kelly"
message_list = []
message_list.append(greeting(name))
message_list += time_and_date("America/New_York")
message_list.append(get_weather("Pittsburgh"))
message_list.append("Here are today's headlines:")
message_list += get_headlines()
message_list.append("Have a great day!")

for m in message_list:
  time.sleep(1)
  print(m)
```

## Finishing the Weather Function

Included in the workshop files is a script that outputs the current weather and the forecasted high/low temperatures for a given location. This script can be passed the name of a city from the commandline using the `--location` flag. For example, if we wanted to get the weather in Chicago, we would run this line:

```bash
python get_weather_info.py --city Chicago
```

Observe the output of running this script for a city of your choice:

```
/content# python get_weather_info.py --city "Chicago, IL"
Weather in: Chicago, IL ([41.8755616, -87.6244212])
Current Temp: 86
Max Temp: 92
Min Temp: 76
```

### Discussion: Inspecting the `get_weather_info.py` script

Open up the `get_weather_info.py` script and explore the contents as you answer these questions:
* In plain language, what is this code doing?
* What elements of this script are similar to the one that we're building?
* Which elements are different?
* How can we use this code to finish our weather message function?

> `get_weather_info.py`:
```python
import openmeteo_requests
import argparse
from geopy.geocoders import Nominatim

def get_city_latlong(city_name):
  geolocator = Nominatim(user_agent="my_city_geocoder")
  location =  geolocator.geocode(city_name)
  if location:
    return [location.latitude, location.longitude]
  else:
    return None

def weather_lookup(coords):
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

  responses = openmeteo.weather_api(url, params = params)

  current_temp = round(responses[0].Current().Variables(0).Value())
  max_temp = round(float(responses[0].Daily().Variables(0).ValuesAsNumpy().max()))
  min_temp = round(float(responses[0].Daily().Variables(1).ValuesAsNumpy().max()))

  return current_temp, max_temp, min_temp

def main():
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
```
