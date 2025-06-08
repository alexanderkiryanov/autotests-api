from pydantic import BaseModel, Field

class Address(BaseModel):
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = Field(alias="isActive")

user_data = {
    "id": "123",
    "name": "Alex",
    "email": "alex@gmail.com",
    "isActive": False,
}
user = User(**user_data)
print(user.model_dump())

