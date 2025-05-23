import httpx
from tools.fakers import get_random_email
from pprint import pprint

# Создание пользователя

create_user_payload = {
  "email": get_random_email(),
  "password": "Identity",
  "lastName": "Ivanov",
  "firstName": "Ivan",
  "middleName": "Ivanovich"
}
response_create_user = httpx.post("http://localhost:8000/api/v1/users",
                                  json=create_user_payload)
response_create_user_data = response_create_user.json()
print(response_create_user.status_code)
print("Пользователь создан")
pprint(response_create_user.json())

# Аутентификация пользователя

login_payload = {
  "email": create_user_payload["email"],
  "password": create_user_payload["password"]
}
response_login = httpx.post("http://localhost:8000/api/v1/authentication/login",
                                  json=login_payload)
response_login_data = response_login.json()
print(response_login.status_code)
print("Пользователь прошел аутентификацию")
pprint(response_login.json())

# Обновление пользователя

update_user_headers = {
    "Authorization": f"Bearer {response_login_data["token"]["accessToken"]}"
}
update_user_payload = {
  "email": get_random_email(),
  "lastName": "Petrov",
  "firstName": "Alexander",
  "middleName": "Alexandrovich"
}

response_update_user = httpx.patch(
    f"http://localhost:8000/api/v1/users/{response_create_user_data["user"]["id"]}",
    headers=update_user_headers,
    json=update_user_payload
)
print(response_update_user.status_code)
print("Пользователь обновлен")
pprint(response_update_user.json())