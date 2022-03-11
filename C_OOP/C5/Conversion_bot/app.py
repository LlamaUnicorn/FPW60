# config.py:

# TOKEN = ''
# WEATHER_TOKEN=''
#
# keys = {
#     'биткоин': 'BTC',
#     'эфириум': 'ETH',
#     'доллар': 'USD',
# }

# TODO: Бот возвращает цену на определённое количество валюты (евро, доллар или рубль).
# TODO: При написании бота необходимо использовать библиотеку pytelegrambotapi.
# TODO: Человек должен отправить сообщение боту в виде <имя валюты, цену которой он хочет узнать> <имя валюты, в которой надо узнать цену первой валюты> <количество первой валюты>.
# TODO: При вводе команды /start или /help пользователю выводятся инструкции по применению бота.
# TODO: При вводе команды /values должна выводиться информация о всех доступных валютах в читаемом виде.
# TODO: Для получения курса валют необходимо использовать API и отправлять к нему запросы с помощью библиотеки Requests.
# TODO: Для парсинга полученных ответов использовать библиотеку JSON.
# TODO: При ошибке пользователя (например, введена неправильная или несуществующая валюта или неправильно введено число) вызывать собственно написанное исключение APIException с текстом пояснения ошибки.
# TODO: Текст любой ошибки с указанием типа ошибки должен отправляться пользователю в сообщения.
# TODO: Для отправки запросов к API описать класс со статическим методом get_price(), который принимает три аргумента и возвращает нужную сумму в валюте:
# TODO: - имя валюты, цену на которую надо узнать, — base;
# TODO: - имя валюты, цену в которой надо узнать, — quote;
# TODO: - количество переводимой валюты — amount.
# TODO: Токен Telegram-бота хранить в специальном конфиге (можно использовать .py файл).
# TODO: Все классы спрятать в файле extensions.py.

# TODO: Перевести пользовательский ввод в lowercase
# TODO: Найти падежи в практикуме
# TODO: Добавить правильные падежи в ответы: 25 доллар_ов = 2566 рублей
# TODO: Добавить погоду

import telebot
from config import keys, TOKEN
from utils import ConvertionException, CryptoConverter

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


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionException('Введите 3 параметра.')

        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя. \n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)

# Add weather


bot.polling()
