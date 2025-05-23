import httpx

# login
login_payload = {
    "email": "rinonorm@gmail.com",
    "password": "Qwerty_122"
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login",
                            json=login_payload)
login_response_data = login_response.json()

print("Login data: ", login_response_data)

# создание клиента + добавление всех переиспользуемых данных в его параметры
client = httpx.Client(
    base_url="http://localhost:8000/api/v1",
    timeout=100,
    headers={"Authorization": f"Bearer {login_response_data["token"]["accessToken"]}"}
)

get_user_me_resp = client.get("/users/me")
get_user_me_resp_data = get_user_me_resp.json()

print("Get user me data: ", get_user_me_resp_data)