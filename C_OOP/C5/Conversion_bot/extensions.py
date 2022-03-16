import json
import requests
from config import keys, WEATHER_TOKEN


class ConversionException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise ConversionException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConversionException(f'Не удалось обработать валюту {quote}.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConversionException(f'Не удалось обработать валюту {base}.')

        try:
            amount = float(amount)
        except ValueError:
            raise ConversionException(f'Не удалось обработать количество {amount}.')

        # r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        r = requests.get(f'https://api.exchangerate.host/convert?from={quote_ticker}&to={base_ticker}&amount={amount}')
        # total_base = json.loads(r.content)[keys[base]]
        # total_base = r.json()
        total_base = json.loads(r.content)['result']
        total_base = round(total_base, 2)
        return total_base


# url = 'https://api.exchangerate.host/convert?from=USD&to=EUR'
# response = requests.get(url)
# data = response.json()
#
# print(data)

# {"motd":{"msg":"If you or your company use this project or like what we doing, please consider backing us so we can "
#                "continue maintaining and evolving this project.","url":"https://exchangerate.host/#/donate"},
#  "success":true,"query":{"from":"USD","to":"EUR","amount":1},"info":{"rate":0.911938},"historical":false,
#  "date":"2022-03-16","result":0.911938}

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
        web_source = f'https://api.openweathermap.org/geo/1.0/direct?q={self._location}&limit=5&appid={WEATHER_TOKEN}&lang=ru'
        r = requests.get(web_source)
        texts = json.loads(r.content)
        # print(texts[0]['local_names']['ru'])
        current_coordinates = f'Lat: {texts[0]["lat"]}, Lon: {texts[0]["lon"]}'
        # print(current_coordinates)
        self.location_lat = texts[0]['lat']
        self.location_lon = texts[0]['lon']

        located_weather = f'https://api.openweathermap.org/data/2.5/weather?lat={self.location_lat}&lon={self.location_lon}&appid={WEATHER_TOKEN}&units=metric'
        weather_request = requests.get(located_weather)
        texts_weather = json.loads(weather_request.content)
        # print(texts_weather)
        weather_report = f"{texts[0]['local_names']['ru']}: ощущается, как {texts_weather['main']['feels_like']}°C."
        print(weather_report)
        return weather_report

    # def run(self):
    #     # g = GetWeather()
    #     # g.location = input('city: ')
    #     g.get_coordinates()
