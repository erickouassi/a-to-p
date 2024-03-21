"""backfill extracted article

Revision ID: 00170ec4ba00
Revises: 75e1809cd8b6
Create Date: 2024-03-20 20:12:32.157977

"""

from typing import Sequence, Union

from alembic import op
import sqlmodel

from api.db import get_session_for_migrations
from api.models import Episode, ExtractedArticleModel
from sqlalchemy.sql.operators import isnot


# revision identifiers, used by Alembic.
revision: str = "00170ec4ba00"
down_revision: Union[str, None] = "75e1809cd8b6"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    session = get_session_for_migrations(bind=op.get_bind())
    articles = (
        session.execute(
            sqlmodel.select(Episode).where(Episode.extracted_article_pydantic != None)
        )
        .scalars()
        .all()
    )
    for episode in articles:
        if not episode.extracted_article_pydantic:
            continue
        print(episode)
        extracted_article = ExtractedArticleModel(
            **episode.extracted_article_pydantic.model_dump()
        )
        session.add(extracted_article)
        episode.extracted_article = extracted_article
        session.add(episode)

    session.commit()

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    # ### end Alembic commands ###
    session = get_session_for_migrations(bind=op.get_bind())
    result = sqlmodel.delete(ExtractedArticleModel).where(
        ExtractedArticleModel.id != None
    )
    session.execute(result)
