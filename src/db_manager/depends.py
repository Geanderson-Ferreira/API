from fastapi import Depends

from src.db_manager.config import SESSION


def get_db_session():
    try:
        session = SESSION()
        yield session
    finally:
        session.close()
