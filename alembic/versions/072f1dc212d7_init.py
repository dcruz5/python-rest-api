"""init

Revision ID: 072f1dc212d7
Revises: 
Create Date: 2023-05-16 07:05:19.159381

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '072f1dc212d7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'products',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String,nullable=False),
        sa.Column('stock', sa.String, nullable=False),
        sa.Column('price', sa.Float,nullable=True),
        sa.Column('brand', sa.String,nullable=True)
    )


def downgrade() -> None:
    op.drop_table('products')