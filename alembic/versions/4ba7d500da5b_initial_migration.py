"""Initial migration

Revision ID: 4ba7d500da5b
Revises: 
Create Date: 2023-03-06 17:38:52.175553

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ba7d500da5b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String),
        sa.Column('email', sa.String),
        sa.Column('password', sa.String),
    )


def downgrade() -> None:
    pass
