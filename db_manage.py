from db import create_tables


def migrate():
    return create_tables()

migrate()
