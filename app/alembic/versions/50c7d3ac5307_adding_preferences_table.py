"""adding extensions and base functions

Revision ID: 50c7d3ac5307
Revises: a23ef2423671
Create Date: 2020-11-02 00:01:02.311660

"""
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

from alembic import op

# revision identifiers, used by Alembic.
revision = "50c7d3ac5307"
down_revision = "a23ef2423671"
branch_labels = None
depends_on = None


# let's create a trigger for running `timestamp_create_dt_func` which is already
# created in inisialising migration script.
# also updated_at column should be updated
TRIGGER_CREATE_DT_SQL = """
        -- created_at
	CREATE TRIGGER
	    preferences_trigger_dt_create
		BEFORE INSERT
		    ON preferences
		    FOR EACH ROW
		    EXECUTE PROCEDURE timestamp_create_dt_func();

        -- updated_at
	CREATE TRIGGER
	    preferences_trigger_dt_insert_update
		BEFORE INSERT
		    ON preferences
		    FOR EACH ROW
		    EXECUTE PROCEDURE timestamp_update_dt_func();
    """

# drop creation triggers
DROP_CREATE_TRIGGER_SQL = """
        DROP TRIGGER IF EXISTS preferences_trigger_dt_create ON preferences;
        DROP TRIGGER IF EXISTS preferences_trigger_dt_insert_update ON preferences;
    """

# like creation trigger, this will also trigger `timestamp_update_dt_func`.
TRIGGER_UPDATE_DT_SQL = """
	CREATE TRIGGER
	    preferences_trigger_dt_update
		BEFORE UPDATE
		    ON preferences
		    FOR EACH ROW
		    EXECUTE PROCEDURE timestamp_update_dt_func();
    """
# drop update trigger
DROP_UPDATE_TRIGGER_SQL = """
        DROP TRIGGER IF EXISTS preferences_trigger_dt_update ON preferences;
    """


def upgrade():
    op.create_table(
        "preferences",
        sa.Column(
            "id", UUID(as_uuid=True), nullable=False, server_default=sa.text("uuid_generate_v4()")
        ),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("value", sa.String(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_preferences_id"), "preferences", ["id"], unique=True)
    op.create_index(op.f("ix_preferences_name"), "preferences", ["name"], unique=True)

    # create createtion trigger
    op.execute(TRIGGER_CREATE_DT_SQL)
    # create update trigger
    op.execute(TRIGGER_UPDATE_DT_SQL)


def downgrade():
    op.drop_index(op.f("ix_preferences_name"), table_name="preferences")
    op.drop_index(op.f("ix_preferences_id"), table_name="preferences")
    op.drop_table("preferences")

    # drop update trigger
    op.execute(DROP_UPDATE_TRIGGER_SQL)
    # drop createtion trigger
    op.execute(DROP_CREATE_TRIGGER_SQL)
