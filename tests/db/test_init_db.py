from src.db.init_db import DatabaseInitializer
from pathlib import Path


def test_initialize_database():
    initializer = DatabaseInitializer()
    initializer.initialize_database()

    assert Path("db/nifty100.db").exists()