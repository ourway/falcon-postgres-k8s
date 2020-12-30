"""adding preferences table

Revision ID: a23ef2423671
Revises:
Create Date: 2020-11-01 23:46:07.170124

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "a23ef2423671"
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

CREATE_DT_FUNC_SQL = """
	CREATE OR REPLACE FUNCTION timestamp_create_dt_func()
	    RETURNS trigger AS
		$$
		    BEGIN
			NEW.created_at = now();
			RETURN NEW;
		    END;
		$$
	LANGUAGE 'plpgsql';
    """
REMOVE_DT_CREATE_FUNC = """
        DROP FUNCTION IF EXISTS timestamp_create_dt_func;
    """

UPDATE_DT_FUNC_SQL = """
	CREATE OR REPLACE FUNCTION timestamp_update_dt_func()
	    RETURNS trigger AS
		$$
		    BEGIN
			NEW.updated_at = now();
			RETURN NEW;
		    END;
		$$
	LANGUAGE 'plpgsql';
    """

REMOVE_DT_UPDATE_FUNC = """
        DROP FUNCTION IF EXISTS timestamp_update_dt_func;
    """


def upgrade():
    # create the os_uuid extension
    op.execute(OS_UUID_EXTENSION_CREATION_SQL)
    op.execute(BTREE_GIST_EXTENSION_CREATION_SQL)
    # create datetime creation function
    op.execute(CREATE_DT_FUNC_SQL)
    # create datetime update function
    op.execute(UPDATE_DT_FUNC_SQL)


def downgrade():
    # remove datetime update function
    op.execute(REMOVE_DT_UPDATE_FUNC)
    # remove datetime creation function
    op.execute(REMOVE_DT_CREATE_FUNC)
    # drop os_uuid extension
    op.execute(BTREE_GIST_EXTENSION_DROP_SQL)
    op.execute(OS_UUID_EXTENSION_DROP_SQL)
