from httpx import Response
from typing import TypedDict
from clients.api_client import APIClient


class GetRequestExercisesDict(TypedDict):
    """
    Описание структуры запроса на получение списка уроков.
    """
    exercisesId: str


class CreateRequestExercisesDict(TypedDict):
    """
    Описание структуры запроса на создание уроков.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateRequestExercisesDict(TypedDict):
    """
    Описание структуры запроса на обновление уроков.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """
    def get_exercises_api(self, query: GetRequestExercisesDict) -> Response:
        """
        Метод получения списка уроков.

        :param query: Словарь с exercisesId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("http://localhost:8000/api/v1/exercises", params=query)

    def get_exercise_api(self, exercises_id: str) -> Response:
        """
        Метод получения урока.

        :param exercises_id: Идентификатор урока.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"http://localhost:8000/api/v1/exercises/{exercises_id}")

    def create_exercise_api(self, request: CreateRequestExercisesDict) -> Response:
        """
        Метод создания урока.

        :param request: Словарь с title, maxScore, minScore, courseId, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("http://localhost:8000/api/v1/exercises", json=request)

    def update_exercise_api(self, exercises_id: str, request: UpdateRequestExercisesDict) -> Response:
        """
        Метод обновления урока.

        :param exercises_id: Идентификатор урока.
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"http://localhost:8000/api/v1/exercises/{exercises_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления урока.

        :param exercises_id: Идентификатор урока.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"http://localhost:8000/api/v1/exercises/{exercise_id}")