import telebot

TOKEN = '5169419362:AAFmsm8W_4fwTCu8VV-xdBoN7LtlhSxFRIs'  # "Токен полученный при регистрации"

bot = telebot.TeleBot(TOKEN)


# @bot.message_handler(filters)
# def function_name(message):
#     bot.reply_to(message, "This is a message handler")


# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
# @bot.message_handler(commands=['start', 'help'])
# def handle_start_help(message):
#     pass


# # Обрабатывается все документы и аудиозаписи
# @bot.message_handler(content_types=['document', 'audio'])
# def handle_docs_audio(message):
#     pass


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Welcome, {message.chat.username}")


@bot.message_handler(content_types=['photo', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')


@bot.message_handler(content_types=['text', ])
def say_hi(message: telebot.types.Message):
    bot.reply_to(message, f"Привет, {message.chat.username}")


# Чтобы запустить бота, нужно воспользоваться методом polling.

bot.polling(none_stop=True)
# Параметр none_stop=True говорит, что бот должен стараться
# не прекращать работу при возникновении каких-либо ошибок.
