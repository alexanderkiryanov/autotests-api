from typing import Self

from fastapi import Query
from pydantic import BaseModel, UUID4, Field, model_validator

from utils.schema.database import DatabaseSchema
from utils.schema.query import QuerySchema


class Exercise(DatabaseSchema):
    id: UUID4
    title: str = Field(max_length=250)
    course_id: UUID4 = Field(alias="courseId")
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    description: str
    order_index: int = Field(alias="orderIndex", default=0)
    estimated_time: str | None = Field(alias="estimatedTime", max_length=50)


class CreateExerciseRequest(BaseModel):
    title: str = Field(max_length=250)
    course_id: UUID4 = Field(alias="courseId")
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    description: str
    order_index: int = Field(alias="orderIndex", default=0)
    estimated_time: str | None = Field(alias="estimatedTime", max_length=50)

    @model_validator(mode='after')
    def validate_model(self) -> Self:
        if self.max_score < self.min_score:
            raise ValueError('max score should not be less than min score')

        return self


class UpdateExerciseRequest(BaseModel):
    title: str | None = Field(default=None, max_length=250)
    max_score: int | None = Field(alias="maxScore", default=None)
    min_score: int | None = Field(alias="minScore", default=None)
    description: str | None = None
    order_index: int | None = Field(alias="orderIndex", default=None)
    estimated_time: str | None = Field(alias="estimatedTime", default=None, max_length=50)

    @model_validator(mode='after')
    def validate_model(self) -> Self:
        if self.max_score < self.min_score:
            raise ValueError('max score should not be less than min score')

        return self


class GetExercisesQuery(QuerySchema):
    course_id: UUID4 = Field(alias="courseId")

    @classmethod
    async def as_query(cls, course_id: UUID4 = Query(alias="courseId")) -> Self:
        return GetExercisesQuery(course_id=course_id)


class GetExerciseResponse(BaseModel):
    exercise: Exercise


class GetExercisesResponse(BaseModel):
    exercises: list[Exercise]
