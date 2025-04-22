from time import time

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship

from lib.db.session import Base


class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    created_at = Column(DateTime, default=time(), nullable=False)
    stories = relationship("Story", back_populates="author")
