from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship

from lib.db.session import Base


class Source(Base):
    __tablename__ = "source"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    country = Column(String, index=True, nullable=False)
    country_code = Column(String, unique=True, index=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    stories = relationship("Story", back_populates="source")
