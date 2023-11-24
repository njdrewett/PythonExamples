#! python3

# This program will perform the following

#1. Reads the requested location from the command line
#2. Downloads JSON weather data from OpenWeatherMap.org
#3. Converts the string of JSON data to a Python data structure
#4. Prints the weather for today and the next two days

APPID = 'd4c9ed839fd1839b7efae63d0e391969'
import json
import requests
import sys

# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()

location = ' '.join(sys.argv[1:])

# TODO: Download the JSON data from OpenWeatherMap.org's API.
# Download the JSON data from OpenWeatherMap.org's API.
url ='https://api.openweathermap.org/data/2.5/forecast?q=%s&cnt=3&appid=%s' % (location, APPID)
print(url)
response = requests.get(url)
response.raise_for_status()

print(response.text)
# TODO: Load JSON data into a Python variable.

