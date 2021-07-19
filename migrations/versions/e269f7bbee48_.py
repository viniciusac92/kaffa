"""empty message

Revision ID: e269f7bbee48
Revises: 3431de699aa1
Create Date: 2021-07-17 21:18:39.037585

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e269f7bbee48'
down_revision = '3431de699aa1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('accounts', sa.Column('total_value', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('accounts', 'total_value')
    # ### end Alembic commands ###
