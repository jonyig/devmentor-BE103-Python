"""create event table

Revision ID: b32815d71bd0
Revises: b75f98bad312
Create Date: 2024-03-05 02:56:19.510526

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b32815d71bd0'
down_revision: Union[str, None] = 'b75f98bad312'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "events",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("date", sa.String(length=255), nullable=False),
        sa.Column("content", sa.String(length=255), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
    )
    pass


def downgrade() -> None:
    op.drop_table("events")
    pass

