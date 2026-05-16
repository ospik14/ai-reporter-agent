from datetime import datetime
from core.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func, DateTime

class Post(Base):
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(primary_key=True)
    image_url: Mapped[str | None] = mapped_column(default=None) 
    title: Mapped[str | None] = mapped_column(default=None)
    text: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        server_default=func.now()
    )
