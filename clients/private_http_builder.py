from httpx import Client
from clients.authentication.authentication_client import LoginRequestDict, get_authentication_client
from typing import TypedDict

class AuthenticationUserDict(TypedDict):
    """
    Структура данных пользователя для аутентификации
    """
    email: str
    password: str


def get_private_http_client(user: AuthenticationUserDict) -> Client:
    """
    Функция создаёт экземпляр httpx.Client с аутентификацией пользователя.

    :param user: Объект AuthenticationUserDict с email и паролем пользователя.
    :return: Готовый к использованию объект httpx.Client с установленным заголовком Authorization.
    """
    # Инициализируем AuthenticationClient для аутентификации
    authentication_client = get_authentication_client()

    # Инициализируем запрос на аутентификацию
    login_request = LoginRequestDict(email=user["email"], password=user["password"])

    # Выполняем post запрос и аутентификацию
    login_response = authentication_client.login(login_request)

    return Client(
        timeout=100,
        base_url="http://localhost:8000",
        headers={"Authorization": f"Bearer {login_response["token"]["accessToken"]}"}
    )