from sqlalchemy.orm import mapped_column, Mapped

from src.models import Base


class Post(Base):
    __tablename__ = 'post'
    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str]