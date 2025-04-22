from lib.db.Base import Story
from lib.logging.logger import LOGGER


def create_story(db, story_data):
    """
    Create a new story in the database.
    """
    story = Story(**story_data)
    LOGGER.info(f"Creating new story: {story.title}")
    db.add(story)
    db.commit()
    db.refresh(story)
