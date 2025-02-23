from enum import Enum


class APIRoutes(str, Enum):
    USERS = '/users'
    COURSES = '/courses'
    EXERCISES = '/exercises'
    AUTHENTICATION = '/authentication'

    def as_tag(self) -> str:
        return self[1:]
