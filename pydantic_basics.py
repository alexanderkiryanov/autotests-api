"""
{
  "course": {
    "id": "string",
    "title": "string",
    "maxScore": 0,
    "minScore": 0,
    "description": "string",
    "previewFile": {
      "id": "string",
      "filename": "string",
      "directory": "string",
      "url": "https://example.com/"
    },
    "estimatedTime": "string",
    "createdByUser": {
      "id": "string",
      "email": "user@example.com",
      "lastName": "string",
      "firstName": "string",
      "middleName": "string"
    }
  }
}
"""
import uuid
from pydantic import BaseModel, Field, ConfigDict, computed_field, HttpUrl, EmailStr, ValidationError
from pydantic.alias_generators import to_camel

# создаем модель файла
class FileSchema(BaseModel):
    id: str
    filename: str
    directory: str
    url: HttpUrl

# создаем модель пользователя
class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

    @computed_field
    def username(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_username(self) -> str:
        return f"{self.first_name} {self.last_name}"

# создаем модель курсов
class CourseSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True) # alias generator

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    # default factory - позволяет генерировать значение на лету
    title: str = "Playwright"
    max_score: int = Field(alias="maxScore", default=1000)
    min_score: int = Field(alias="minScore", default=100)
    description: str = "Playwright course"
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime", default="2 weeks")
    created_by_user: UserSchema = Field(alias="createdByUser")

# передаем данные в модель и выводим
course_default_model = CourseSchema(
    id="course-id",
    title="Playwright",
    maxScore=100,
    minScore=10,
    description="Playwright",
    estimatedTime="1 week",
    previewFile=FileSchema(
        id="file-id",
        filename="yasna.png",
        directory="courses",
        url="http://localhost:8000"
    ),
    createdByUser=UserSchema(
        id="user-id",
        email="user@gmail.com",
        lastName="Bond",
        firstName="Zara",
        middleName="Alice"
    )
)
print("Course default model: ", course_default_model)

# распаковка словаря
course_dict = {
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 0,
    "description": "Playwright",
    "estimatedTime": "1 week",
    "previewFile": {
        "id": "file-id",
        "filename": "yasna.png",
        "directory": "courses",
        "url": "http://localhost:8000"
    },
    "createdByUser": {
        "id": "user-id",
        "email": "user@gmail.com",
        "lastName": "Bond",
        "firstName": "Zara",
        "middleName": "Alice"
    }
}
course_dict_model = CourseSchema(**course_dict)
print("Course dict model: ",course_default_model)

# парсинг JSON (десериализация)
course_json = """
{
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 0,
    "description": "Playwright",
    "estimatedTime": "1 week",
    "previewFile": {
        "id": "file-id",
        "filename": "yasna.png",
        "directory": "courses",
        "url": "http://localhost:8000"
    },
    "createdByUser": {
        "id": "user-id",
        "email": "user@gmail.com",
        "lastName": "Bond",
        "firstName": "Zara",
        "middleName": "Alice"
    }
}
"""
course_json_model = CourseSchema.model_validate_json(course_json)
print("Course json model: ", course_json_model)

# сериализация pydantic model в json
print(course_json_model.model_dump(by_alias=True))
print(course_json_model.model_dump_json(by_alias=True))

user = UserSchema(
    id="user-id",
    email="user@gmail.com",
    lastName="Bond",
    firstName="Zara",
    middleName="Alice"
)
print(user.get_username(), user.username)

try:
    file = FileSchema(
        id="file-id",
        filename="yasna.png",
        directory="courses",
        url="http://localhost:8000"
    )
except ValidationError as error:
    print(error)
    print(error.errors())

print(file)

