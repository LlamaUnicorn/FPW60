import requests

r = requests.get(
    'https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html')
# делаем запрос на сервер по переданному адресу
print(r.content)
print("Status:", r.status_code)

# Запрос в JSON

# import requests

r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')  # попробуем поймать json-ответ
print(r.content)
