"""create user table

Revision ID: 847d1fbc4d74
Revises: 30c501099ca3
Create Date: 2024-02-24 01:59:45.965543

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '847d1fbc4d74'
down_revision: Union[str, None] = '30c501099ca3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "notify",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(length=255), nullable=False),)
    pass


def downgrade() -> None:
    op.drop_table("notify")
    pass
