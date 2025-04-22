from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from lib.db.session import Base


class NewsSource(Base):
    __tablename__ = "news_source"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    country = Column(String, index=True, nullable=False)
    country_code = Column(String, unique=True, index=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
