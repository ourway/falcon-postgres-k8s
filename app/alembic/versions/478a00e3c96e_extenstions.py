"""extenstions

Revision ID: 478a00e3c96e
Revises: 
Create Date: 2020-12-29 08:02:12.900845

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "478a00e3c96e"
down_revision = None
branch_labels = None
depends_on = None


OS_UUID_EXTENSION_CREATION_SQL = """
        CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
    """
OS_UUID_EXTENSION_DROP_SQL = """
        DROP EXTENSION IF EXISTS "uuid-ossp";
    """

BTREE_GIST_EXTENSION_CREATION_SQL = """
        CREATE EXTENSION IF NOT EXISTS "btree_gist";
    """
BTREE_GIST_EXTENSION_DROP_SQL = """
        DROP EXTENSION IF EXISTS "btree_gist";
    """


def upgrade():
    op.execute(OS_UUID_EXTENSION_CREATION_SQL)
    op.execute(BTREE_GIST_EXTENSION_CREATION_SQL)


def downgrade():
    op.execute(BTREE_GIST_EXTENSION_DROP_SQL)
    op.execute(OS_UUID_EXTENSION_DROP_SQL)
