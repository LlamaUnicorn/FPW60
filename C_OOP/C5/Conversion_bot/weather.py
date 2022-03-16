import json
import requests
# Weather works fine
# https://openweathermap.org/
TOKEN = ''

user_location = input('Укажите город: ')
web_source = f'https://api.openweathermap.org/geo/1.0/direct?q={user_location}&limit=5&appid={TOKEN}&lang=ru'
r = requests.get(web_source)
texts = json.loads(r.content)
# for text in texts:
#     print(text, '\n')

# Get city location coordinates (lat, lon)
print('-' * 10)
print(texts[0]['local_names']['ru'])
current_coordinates = f'Lat: {texts[0]["lat"]}, Lon: {texts[0]["lon"]}'
print(current_coordinates)
location_lat = texts[0]['lat']
location_lon = texts[0]['lon']

# Pass location coordinates to get the weather
located_weather = f'https://api.openweathermap.org/data/2.5/weather?lat={location_lat}&lon={location_lon}&appid={TOKEN}&units=metric'
weather_request = requests.get(located_weather)
texts_weather = json.loads(weather_request.content)
weather_report = f"Ощущается как: {texts_weather['main']['feels_like']}°C"
print(weather_report)

# ends here