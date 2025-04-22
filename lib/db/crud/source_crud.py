from lib.db.Base import Source

from lib.logging.logger import LOGGER


def create_source(db, news_source_data):
    """
    Create a new news source in the database.
    """
    news_source = Source(**news_source_data)
    LOGGER.info(f"Creating new source: {news_source.name}")
    db.add(news_source)
    db.commit()
    db.refresh(news_source)
    return news_source


def get_source_by_name(db, name):
    """
    Get a news source by its name.
    """
    LOGGER.info(f"Getting source by name: <{name}>")
    return db.query(Source).filter(Source.name == name).first()
