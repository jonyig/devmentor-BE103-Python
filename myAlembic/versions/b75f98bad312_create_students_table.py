"""create student table

Revision ID: b75f98bad312
Revises: 5bdf6ac77518
Create Date: 2024-03-05 02:55:20.821263

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b75f98bad312'
down_revision: Union[str, None] = '5bdf6ac77518'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "students",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("sex", sa.String(length=1), nullable=False),
    )
    pass


def downgrade() -> None:
    op.drop_table("students")
    pass

