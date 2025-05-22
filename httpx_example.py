import httpx
from pprint import pprint

# отправка GET-запроса
response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")

print(response.status_code)
print(response.json())
# response.json() — парсит JSON-ответ

# отправка POST-запроса
data = {
    "title": "Новая задача",
    "completed": False,
    "userId": 1
}

response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)
# json=data - автоматически сериализует Python-словарь в JSON

print(response.status_code)
print(response.request.headers)
print(response.json())

# Отправка данных в application/x-www-form-urlencoded
data = {"username": "test_data", "password": "123456"}

response = httpx.post("https://httpbin.org/post", data=data)

print(response.status_code)
pprint(response.json())

# передача хедеров в запрос
headers = {"Authentication": "Bearer my_secret_token"}
response = httpx.get("https://httpbin.org/get", headers=headers)

print(response.request.headers)
pprint(response.json())

# передача параметров в запрос - метод params добавляет параметры к URL, аналогично ?key=value
params = {"userId": 1}
response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)

print(response.url)

# удобный вывод json через pprint
pprint(response.json())

# передача файлов
files = {
    "file": ("example.txt", open("example.txt", "rb"))
}
response = httpx.post("https://httpbin.org/post", files=files)

print(response.json())

# работа с сессиями
# при множественных запросах к API лучше использовать httpx.Client()
# который повторно использует соединения, уменьшая накладные расходы

with httpx.Client() as client:
    response_1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
    response_2 = client.get("https://jsonplaceholder.typicode.com/todos/2")

print(response_1.json())
print(response_2.json())

# добавление базовых заголовков в Client
# передача заголовков во все интересующие нас запросы
client = httpx.Client(headers={"Authentication": "Bearer my_secret_token"})
response = client.get("https://httpbin.org/get")

print(response.json())

# работа с ошибками
# проверка статуса ответа (raise_for_status)
try :
    response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")
    response.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f"Ошибка запроса: {e}")

# обработка таймаутов
try:
    response = httpx.get("https://httpbin.org/delay/5", timeout=2)
except httpx.ReadTimeout:
    print("Запрос превысил лимит времени")