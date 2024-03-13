"""create langs table

Revision ID: 6ee92ebd85c7
Revises: 9ec061e0460e
Create Date: 2024-03-07 02:02:13.196826

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6ee92ebd85c7'
down_revision: Union[str, None] = '9ec061e0460e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "langs",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("lang_name", sa.String(length=255), nullable=False),
    )
    pass


def downgrade() -> None:
    op.drop_table("langs")
    pass
