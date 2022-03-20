# Weather reports
import requests
import json

TOKEN = ''


class GetWeather:
    def __init__(self, city):
        self._location = city
        self.location_lat = None
        self.location_lon = None

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        if isinstance(value, str):
            self._location = value
        else:
            raise ValueError('Значение должно быть строкой')

    def get_coordinates(self):
        # Get city location coordinates (lat, lon)
        web_source = f'https://api.openweathermap.org/geo/1.0/direct?q={self._location}&limit=5&appid={TOKEN}&lang=ru'
        r = requests.get(web_source)
        texts = json.loads(r.content)
        # print(texts[0]['local_names']['ru'])
        current_coordinates = f'Lat: {texts[0]["lat"]}, Lon: {texts[0]["lon"]}'
        # print(current_coordinates)
        self.location_lat = texts[0]['lat']
        self.location_lon = texts[0]['lon']

        located_weather = f'https://api.openweathermap.org/data/2.5/weather?lat={self.location_lat}&lon={self.location_lon}&appid={TOKEN}&units=metric'
        weather_request = requests.get(located_weather)
        texts_weather = json.loads(weather_request.content)
        # print(texts_weather)
        weather_report = f"{texts[0]['local_names']['ru']}: ощущается, как {texts_weather['main']['feels_like']}°C."
        print(weather_report)
        return weather_report

    @staticmethod
    def run(self):
        # g.location = input('city: ')
        self.get_coordinates()


# g = GetWeather('Москва')
# # g.get_coordinates()
# g.run()


# ------------------------------------------------
# works with classes. can't pass input into bot

# Weather reports
# import requests
# import json
#
# TOKEN = '8fe93768c7de158a7ff19f41373800df'
#
#
# class GetWeather:
#     def __init__(self):
#         self._location = None
#         self.location_lat = None
#         self.location_lon = None
#
#     @property
#     def location(self):
#         return self._location
#
#     @location.setter
#     def location(self, value):
#         if isinstance(value, str):
#             self._location = value
#         else:
#             raise ValueError('Значение должно быть строкой')
#
#     def get_coordinates(self):
#         # Get city location coordinates (lat, lon)
#         web_source = f'https://api.openweathermap.org/geo/1.0/direct?q={self.location}&limit=5&appid={TOKEN}&lang=ru'
#         r = requests.get(web_source)
#         texts = json.loads(r.content)
#         # print(texts[0]['local_names']['ru'])
#         current_coordinates = f'Lat: {texts[0]["lat"]}, Lon: {texts[0]["lon"]}'
#         # print(current_coordinates)
#         self.location_lat = texts[0]['lat']
#         self.location_lon = texts[0]['lon']
#
#         located_weather = f'https://api.openweathermap.org/data/2.5/weather?lat={self.location_lat}&lon={self.location_lon}&appid={TOKEN}&units=metric'
#         weather_request = requests.get(located_weather)
#         texts_weather = json.loads(weather_request.content)
#         # print(texts_weather)
#         weather_report = f"{texts[0]['local_names']['ru']}: ощущается, как {texts_weather['main']['feels_like']}°C."
#         print(weather_report)
#         return weather_report
#
#     def run(self):
#         g.location = input('city: ')
#         g.get_coordinates()
#
#
# g = GetWeather()
# g.run()



# ------------------------------------------------

# g.location = input('city: ')
# g.get_coordinates()

# # Weather works fine
# # https://openweathermap.org/
# TOKEN = ''

# user_location = input('Укажите город: ')
# web_source = f'https://api.openweathermap.org/geo/1.0/direct?q={user_location}&limit=5&appid={TOKEN}&lang=ru'
# r = requests.get(web_source)
# texts = json.loads(r.content)
# # for text in texts:
# #     print(text, '\n')

# # Get city location coordinates (lat, lon)
# print('-' * 10)
# print(texts[0]['local_names']['ru'])
# current_coordinates = f'Lat: {texts[0]["lat"]}, Lon: {texts[0]["lon"]}'
# print(current_coordinates)
# location_lat = texts[0]['lat']
# location_lon = texts[0]['lon']

# # Pass location coordinates to get the weather
# located_weather = f'https://api.openweathermap.org/data/2.5/weather?lat={location_lat}&lon={location_lon}&appid={TOKEN}&units=metric'
# weather_request = requests.get(located_weather)
# texts_weather = json.loads(weather_request.content)
# weather_report = f"Ощущается как: {texts_weather['main']['feels_like']}°C"
# print(weather_report)

# ends here

# API returns location like this:


# response = [{"name":"Vladimir","local_names":{"be":"Уладзімір","io":"Vladimir","et":"Vladimir","nl":"Vladimir","gl":"Vladimir","sr":"Владимир","ar":"فلاديمير","af":"Wladimir","en":"Vladimir","da":"Vladimir","ca":"Vladímir","vi":"Vladimir","uk":"Володимир","es":"Vladímir","ja":"ウラジーミル","bg":"Владимир","ru":"Владимир","id":"Vladimir","ka":"ვლადიმირი","it":"Vladimir","eo":"Vladimir","ro":"Vladimir","no":"Vladimir","ky":"Владимир","ko":"블라디미르","cv":"Владимир","os":"Владимир","sv":"Vladimir","la":"Volodimiria","he":"ולדימיר","cs":"Vladimir","hr":"Vladimir","ce":"Владимир","tl":"Vladimir","lv":"Vladimira","fi":"Vladimir","sl":"Vladimir","fr":"Vladimir","lt":"Vladimiras","de":"Wladimir","tr":"Vladimir","mn":"Владимир","br":"Vladimir","zh":"弗拉基米尔","hu":"Vlagyimir","mk":"Владимир","fa":"ولادیمیر (شهر)","uz":"Vladimir","pt":"Vladimir","sk":"Vladimír","ku":"Vladîmîr","el":"Βλαντίμιρ","oc":"Vladímir","qu":"Vladimir","nn":"Vladimir","fy":"Vladimir","pl":"Włodzimierz","eu":"Vladimir"},"lat":56.1288899,"lon":40.4075203,"country":"RU","state":"Vladimir Oblast"},{"name":"Vladimir","local_names":{"ro":"Vladimir","uk":"Владімір"},"lat":44.8277332,"lon":23.5659752,"country":"RO"},{"name":"Vladimir","local_names":{"ro":"Vladimir","uk":"Владімір"},"lat":44.5020451,"lon":23.7611829,"country":"RO"},{"name":"Vladimir","local_names":{"en":"Vladimir","sq":"Katërkollë","sr":"Владимир","uk":"Владімір"},"lat":42.0050689,"lon":19.3052089,"country":"ME"},{"name":"Vladimir","lat":44.8181421,"lon":23.559208826628268,"country":"RO"}]

# print(response[0]['name'])
# print('Printing expected result:', response[0]['local_names']['ru'])
# user_input = input('Your location: ')

# if user_input in response[0]['local_names']['ru']:
#     print('Yeap, it\'s in a list')

# print(response[0]['local_names']['en'])


# API returns weather like this:

# weather_report = {"coord":{"lon":40.41,"lat":56.13},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"base":"stations","main":{"temp":-6.5,"feels_like":-12.21,"temp_min":-6.5,"temp_max":-6.5,"pressure":1036,"humidity":73,"sea_level":1036,"grnd_level":1016},"visibility":10000,"wind":{"speed":3.93,"deg":27,"gust":7.04},"clouds":{"all":9},"dt":1646917384,"sys":{"country":"RU","sunrise":1646884065,"sunset":1646924993},"timezone":10800,"id":473247,"name":"Vladimir","cod":200}

# print(weather_report['main']['feels_like'])
