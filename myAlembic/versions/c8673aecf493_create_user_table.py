"""create user table

Revision ID: c8673aecf493
Revises: 7eef2e0789cb
Create Date: 2024-02-24 01:19:55.375258

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c8673aecf493'
down_revision: Union[str, None] = '7eef2e0789cb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "language",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(length=255), nullable=False),
    )
    pass

def downgrade() -> None:
    op.drop_table("language")
    pass
