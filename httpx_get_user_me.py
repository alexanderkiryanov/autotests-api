import httpx

created_user = {
    "email": "rinonorm@gmail.com",
    "password": "Qwerty_122"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=created_user)
login_response.raise_for_status()

print(login_response.status_code)
print(login_response.json())

token = login_response.json()["token"]["accessToken"]
client = httpx.Client(headers={"Authorization": f"Bearer {token}"})
response_users_me = client.get("http://localhost:8000/api/v1/users/me")
response_users_me.raise_for_status()

print(response_users_me.status_code)
print(response_users_me.json())