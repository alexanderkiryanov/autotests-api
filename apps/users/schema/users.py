from pydantic import UUID4, EmailStr, BaseModel, Field

from utils.schema.database import DatabaseSchema


class User(DatabaseSchema):
    id: UUID4
    email: EmailStr = Field(max_length=250)
    last_name: str = Field(alias="lastName", max_length=50)
    first_name: str = Field(alias="firstName", max_length=50)
    middle_name: str = Field(alias="middleName", max_length=50)


class CreateUserRequest(BaseModel):
    email: EmailStr = Field(max_length=250)
    password: str = Field(max_length=250)
    last_name: str = Field(alias="lastName", max_length=50)
    first_name: str = Field(alias="firstName", max_length=50)
    middle_name: str = Field(alias="middleName", max_length=50)


class UpdateUserRequest(BaseModel):
    email: EmailStr | None = Field(default=None, max_length=250)
    password: str | None = Field(default=None, max_length=250)
    last_name: str | None = Field(alias="lastName", default=None, max_length=50)
    first_name: str | None = Field(alias="firstName", default=None, max_length=50)
    middle_name: str | None = Field(alias="middleName", default=None, max_length=50)


class GetUserResponse(BaseModel):
    user: User
