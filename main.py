"""
Форматы представления данных, JSON, YAML, XML/SOAP
Знакомство с pydantic
Знакомство с pydantic-settings
Написание API клиентов
Знакомстов с Swagger
Знакомство с протоколами
HTTP протокол, коды ответов
gRPC пртокол, прото контракты
WebSocket
TCP/IP протоколы
Про авторизацию а утентификацию, идентификацию
Валидация схемы
Покрытие API автотестами, можно разобрать ту библиотеку, которую сделал артем ерошенко
Про взаимодействие с базой данных, про raw sql, про sqlalchemy

TODO может не обязательно это куда-то деплоить? Можно и настроить локально, нужно подумать
"""
from fastapi import FastAPI

from apps.courses.api import courses_app_router
from apps.exercises.api import exercises_app_router
from apps.users.api import users_app_router
from utils.clients.database.engine import create_database

app = FastAPI(title="QA Automation engineer course API")

app.include_router(users_app_router, prefix="/api/v1")
app.include_router(courses_app_router, prefix="/api/v1")
app.include_router(exercises_app_router, prefix="/api/v1")


@app.on_event("startup")
async def startup_event():
    await create_database()
