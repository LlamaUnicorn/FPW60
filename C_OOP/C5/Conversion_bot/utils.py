import json
import requests
from config import keys


class ConvertionException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}.')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}.')

        # r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        r = requests.get(f'https://api.exchangerate.host/convert?from={quote_ticker}&to={base_ticker}&amount={amount}')
        # total_base = json.loads(r.content)[keys[base]]
        total_base = r.json()

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