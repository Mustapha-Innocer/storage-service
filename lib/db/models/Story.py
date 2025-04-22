from time import time
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from lib.db.session import Base


class Story(Base):
    __tablename__ = "story"

    id = Column(Integer, primary_key=True, index=True)
    source_id = Column(Integer, ForeignKey("source.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("category.id"), nullable=False)
    author_id = Column(Integer, ForeignKey("author.id"), nullable=False)
    url = Column(String, unique=True, nullable=False)
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)
    image_url = Column(String, nullable=False)
    author = relationship("Author", back_populates="stories")
    summary = Column(String, nullable=False)
    published_at = Column(Integer, nullable=False)
    category = relationship("Category", back_populates="stories")
    source = relationship("Source", back_populates="stories")
    created_at = Column(Integer, default=time(), nullable=False)
