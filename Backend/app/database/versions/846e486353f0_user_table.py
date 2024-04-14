"""User Table

Revision ID: 846e486353f0
Revises: 
Create Date: 2024-04-13 18:13:08.855688

"""

import datetime
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import text

from app.choice.user import ROLE

# revision identifiers, used by Alembic.
revision: str = "846e486353f0"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "user",
        sa.Column(
            "id",
            sa.UUID,
            primary_key=True,
            nullable=False,
            server_default=text("gen_random_uuid()"),
        ),
        sa.Column("nick_name", sa.String(length=255), nullable=True),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("password", sa.String(length=255), nullable=False),
        sa.Column("first_name", sa.String(length=255), nullable=False),
        sa.Column("last_name", sa.String(length=255), nullable=False),
        sa.Column("phone_number", sa.String(length=255), nullable=True),
        sa.Column("role", sa.String(length=255), nullable=False, default=ROLE.NORMAL),
        sa.Column(
            "created_at", sa.DateTime(), nullable=False, default=datetime.datetime.now()
        ),
        sa.Column(
            "updated_at", sa.DateTime(), nullable=False, default=datetime.datetime.now()
        ),
    )


def downgrade() -> None:
    op.drop_table("user")
