import redis
import json

red = redis.Redis(
    host='хост',
    port=порт,
    password='пароль'
)

red.delete('dict1')  # удаляются ключи с помощью метода .delete()
print(red.get('dict1'))