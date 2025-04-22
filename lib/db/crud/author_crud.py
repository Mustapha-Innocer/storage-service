from lib.db.Base import Author


def get_author_by_name(db, name):
    """
    Get an author by name.
    """
    return db.query(Author).filter(Author.name == name).first()


def create_author(db, author):
    """
    Create a new author.
    """
    db_author = Author(name=author)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author
