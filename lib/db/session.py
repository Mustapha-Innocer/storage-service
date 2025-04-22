from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from lib.config import config

Base = declarative_base()

SQLALCHEMY_DATABASE_URL = config.DB_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()


def get_db():
    try:
        yield db
    finally:
        db.close()
