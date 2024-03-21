"""free up the name

Revision ID: 26b53c372d47
Revises: 8eaf28088582
Create Date: 2024-03-20 19:44:23.622725

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "26b53c372d47"
down_revision: Union[str, None] = "8eaf28088582"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "episode", "extracted_article", new_column_name="extracted_article_pydantic"
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "episode", "extracted_article_pydantic", new_column_name="extracted_article"
    )
    # ### end Alembic commands ###
