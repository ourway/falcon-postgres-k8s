"""
code related to creating a session
"""
import typing as t
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from utils import get_database_url

engine = create_engine(get_database_url(), echo=False, pool_size=10)
Session = sessionmaker(bind=engine)


@contextmanager
def session_scope() -> t.Any:
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
