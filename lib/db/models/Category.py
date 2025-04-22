from time import time

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from lib.db.session import Base


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    created_at = Column(Integer, default=time(), nullable=False)
    stories = relationship("Story", back_populates="category")
