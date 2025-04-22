from lib.db.Base import Category


def get_category_by_name(db, name):
    """
    Get a category by name.
    """
    return db.query(Category).filter(Category.name == name).first()


def create_category(db, category):
    """
    Create a new category.
    """
    db_category = Category(name=category)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category
