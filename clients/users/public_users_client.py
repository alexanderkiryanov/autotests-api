from clients.api_client import APIClient
import httpx
from typing import TypedDict
from clients.public_http_builder import get_public_http_client

class UserRequestDict(TypedDict):
    """
    Описание структуры запроса для создания нового пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str
    """
    Название ключей (lastName, firstName, middleName) совпадает с API.
    """


class PublicUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """
    def create_user_api(self, request: UserRequestDict) -> httpx.Response:
        """
        Метод выполняет создание нового пользователя.

        :param request: Словарь с email, password, lastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request)

def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client)