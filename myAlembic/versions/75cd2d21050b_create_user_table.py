"""create user table

Revision ID: 75cd2d21050b
Revises: 1d12680ee7c7
Create Date: 2024-02-24 01:52:40.411878

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '75cd2d21050b'
down_revision: Union[str, None] = '1d12680ee7c7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "event_list",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("event_id", sa.Integer(), nullable=False),
    )
    pass


def downgrade() -> None:
    op.drop_table("event_list")
    pass
