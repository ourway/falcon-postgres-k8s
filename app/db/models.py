"""
database models will sit here
"""
from datetime import datetime
from uuid import uuid4

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ENUM, JSONB, TSRANGE, UUID
from sqlalchemy.ext.declarative import declared_attr

from db.base_class import Base


class Preferences(Base):
    """Preferences table:
    To be used for saving platform Preferences.
    """

    id = sa.Column(
        UUID(as_uuid=True),
        primary_key=True,
        index=True,
        default=uuid4,
        unique=True,
        nullable=False,
    )
    name = sa.Column(sa.String, unique=True, nullable=False)
    description = sa.Column(sa.String, nullable=True)
    value = sa.Column(sa.String, nullable=True)
    created_at = sa.Column(sa.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = sa.Column(sa.DateTime, nullable=False, default=datetime.utcnow)

    @declared_attr
    def __tablename__(cls) -> str:  # pylint: disable=no-self-argument
        return "preferences"

    def __str__(self) -> str:
        return f"Preferences: {self.name}: {self.value}"

    def __repr__(self) -> str:
        return repr(str(self))

    def __init__(self, *, name: str, value: str, description: str) -> None:
        """ Initialise a new Preference record """
        self.name = name
        self.value = value
        self.description = description
        return None
