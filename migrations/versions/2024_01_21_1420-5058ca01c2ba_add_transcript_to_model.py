"""add transcript to model

Revision ID: 5058ca01c2ba
Revises: 07cdb4ce4166
Create Date: 2024-01-21 14:20:13.228855

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = "5058ca01c2ba"
down_revision: Union[str, None] = "07cdb4ce4166"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("episode", sa.Column("transcript", sqlmodel.JSON, nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("episode", "transcript")
    # ### end Alembic commands ###
