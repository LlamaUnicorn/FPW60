# config.py:

# TOKEN = ''
# WEATHER_TOKEN=''
#
# keys = {
#     'биткоин': 'BTC',
#     'эфириум': 'ETH',
#     'доллар': 'USD',
# }

# TODO: При написании бота необходимо использовать библиотеку pytelegrambotapi.
# TODO: При ошибке пользователя (например, введена неправильная или несуществующая валюта или неправильно введено число) вызывать собственно написанное исключение APIException с текстом пояснения ошибки.
# DONE: Для отправки запросов к API описать класс со статическим методом get_price(), который принимает три аргумента и возвращает нужную сумму в валюте:
# TODO: Токен Telegram-бота хранить в специальном конфиге (можно использовать .py файл).
# DONE: Все классы спрятать в файле extensions.py.
# TODO: Найти падежи в практикуме
# TODO: Добавить правильные падежи в ответы: 25 доллар_ов = 2566 рублей
# TODO: Добавить погоду. Как передать аргумент города в вызов функции?
# TODO: реализовать асинхронщину, чтобы программа не падала, не дождавшись ответа

# DONE: Бот возвращает цену на определённое количество валюты (евро, доллар или рубль).
# DONE: Человек должен отправить сообщение боту в виде <имя валюты, цену которой он хочет узнать> <имя валюты, в которой надо узнать цену первой валюты> <количество первой валюты>.
# DONE: При вводе команды /start или /help пользователю выводятся инструкции по применению бота.
# DONE: При вводе команды /values должна выводиться информация о всех доступных валютах в читаемом виде.
# DONE: Для получения курса валют необходимо использовать API и отправлять к нему запросы с помощью библиотеки Requests.
# DONE: Для парсинга полученных ответов использовать библиотеку JSON.
# DONE: Текст любой ошибки с указанием типа ошибки должен отправляться пользователю в сообщения.
# DONE: - имя валюты, цену на которую надо узнать, — base;
# DONE: - имя валюты, цену в которой надо узнать, — quote;
# DONE: - количество переводимой валюты — amount.
# DONE: Перевести пользовательский ввод в lowercase

# https://exchangerate.host/#/#articles 
# amount	[optional] The amount to be converted.
# example:amount=1200

import telebot
from config import keys, TOKEN, WEATHER_TOKEN
from extensions import ConversionException, CurrencyConverter, GetWeather

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу, введите команду в следующем формате:\n<имя валюты> \
<в какую валюту перевести> \
<количество переводимой валюты>\nУвидеть список всех доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(commands=['weather', 'погода'])
def weather(message: telebot.types.Message):
    text = 'Погода скоро будет'
    get_weather = GetWeather('Moscow')
    result = get_weather.get_coordinates()
    print(result)
    bot.reply_to(message, result)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConversionException('Введите 3 параметра.')

        quote, base, amount = values
        quote = quote.lower()
        base = base.lower()
        total_base = CurrencyConverter.get_price(quote, base, amount)
    except ConversionException as e:
        bot.reply_to(message, f'Ошибка пользователя. \n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling()
