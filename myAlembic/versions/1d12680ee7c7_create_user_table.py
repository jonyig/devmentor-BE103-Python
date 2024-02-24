"""create user table

Revision ID: 1d12680ee7c7
Revises: c8673aecf493
Create Date: 2024-02-24 01:49:36.387469

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1d12680ee7c7'
down_revision: Union[str, None] = 'c8673aecf493'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("lang_id", sa.Integer(), nullable=False),
    )
    pass


def downgrade() -> None:
    op.drop_table("user")
    pass
