"""create event_list table

Revision ID: 9ec061e0460e
Revises: b32815d71bd0
Create Date: 2024-03-05 02:57:48.544586

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9ec061e0460e'
down_revision: Union[str, None] = 'b32815d71bd0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users_events",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("event_id", sa.Integer(), nullable=False),
    )
    pass


def downgrade() -> None:
    op.drop_table("users_events")
    pass

