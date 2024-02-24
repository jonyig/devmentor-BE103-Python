"""create user table

Revision ID: 30c501099ca3
Revises: 46424abc8a7e
Create Date: 2024-02-24 01:57:31.213904

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '30c501099ca3'
down_revision: Union[str, None] = '46424abc8a7e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "event-lang",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("content", sa.String(length=255), nullable=False),
        sa.Column("event_id", sa.Integer(), nullable=False),
        sa.Column("lang_id", sa.Integer(), nullable=False),
    )
    pass


def downgrade() -> None:
    op.drop_table("event-lang")
    pass
