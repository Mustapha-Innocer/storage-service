from lib.db.Base import Source

from lib.logging.logger import LOGGER


def create_source(db, source_data):
    """
    Create a new news source in the database.
    """
    source = Source(**source_data)
    LOGGER.info(f"Creating new source: {source.name}")
    db.add(source)
    db.commit()
    db.refresh(source)
    return source


def get_source_by_name(db, name):
    """
    Get a news source by its name.
    """
    LOGGER.info(f"Getting source by name: <{name}>")
    return db.query(Source).filter(Source.name == name).first()
