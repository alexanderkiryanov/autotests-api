import uuid

from sqlalchemy import Column, UUID, String, Text, ForeignKey, Integer
from sqlalchemy.orm import Mapped

from utils.clients.database.mixin_model import MixinModel


class CoursesModel(MixinModel):
    __tablename__ = "courses"

    id: Mapped[uuid.UUID] = Column(UUID, nullable=False, primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = Column(String(length=250), nullable=False)
    max_score: Mapped[int] = Column(Integer, nullable=True)
    min_score: Mapped[int] = Column(Integer, nullable=True)
    description: Mapped[str] = Column(Text, nullable=False)
    estimated_time: Mapped[str] = Column(String(length=50), nullable=True)

    created_by_user_id: Mapped[uuid.UUID] = Column(
        UUID,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )
