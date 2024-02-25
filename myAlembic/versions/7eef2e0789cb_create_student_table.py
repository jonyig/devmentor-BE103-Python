"""create user table

Revision ID: 7eef2e0789cb
Revises: 
Create Date: 2024-02-15 00:03:34.782985

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7eef2e0789cb'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "student",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("sex", sa.String(length=1), nullable=False),
    )
    pass


def downgrade() -> None:
    op.drop_table("student")
    pass
