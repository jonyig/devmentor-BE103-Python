"""create user table

Revision ID: 46424abc8a7e
Revises: 75cd2d21050b
Create Date: 2024-02-24 01:54:48.459128

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '46424abc8a7e'
down_revision: Union[str, None] = '75cd2d21050b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "event",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("date", sa.String(length=255), nullable=False),
        sa.Column("content", sa.String(length=255), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("notify_id", sa.Integer(), nullable=False),
    )
    pass


def downgrade() -> None:
    op.drop_table("event")
    pass
