"""create events_langs table

Revision ID: b26a6ace9a35
Revises: 6ee92ebd85c7
Create Date: 2024-03-07 02:02:33.904577

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b26a6ace9a35'
down_revision: Union[str, None] = '6ee92ebd85c7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "events_langs",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("event_id", sa.Integer(), nullable=False),
        sa.Column("lang_id", sa.Integer(), nullable=False),
    )
    pass


def downgrade() -> None:
    op.drop_table("events_langs")
    pass
