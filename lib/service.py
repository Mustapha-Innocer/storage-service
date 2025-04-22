from lib.db.crud import author_crud, category_crud, source_crud, story_crud
from lib.logging.logger import LOGGER


def save(db, news_data):
    """
    Save the news data to the database.
    """
    # Check if news source does not exist and create it.
    story_source = news_data.pop("source")
    source_from_db = source_crud.get_source_by_name(db, story_source["name"])
    if not source_from_db:
        LOGGER.info(f"Source <{story_source["name"]}> not found.")
        source_from_db = source_crud.create_source(db, story_source)

    # Check if news category does not exist and create it.
    story_category = news_data.pop("category")
    category_from_db = category_crud.get_category_by_name(db, story_category)
    if not category_from_db:
        LOGGER.info(f"Category <{story_category}> not found.")
        category_from_db = category_crud.create_category(db, story_category)

    # Check if news author does not exist and create it.
    story_author = news_data.pop("author")
    author_from_db = author_crud.get_author_by_name(db, story_author)
    if not author_from_db:
        LOGGER.info(f"Author <{story_author}> not found.")
        author_from_db = author_crud.create_author(db, story_author)

    # Update the news data with the IDs from the database.
    news_data["source_id"] = source_from_db.id
    news_data["category_id"] = category_from_db.id
    news_data["author_id"] = author_from_db.id

    story_crud.create_story(db, news_data)
