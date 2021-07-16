"""empty message

Revision ID: 0fb6bd0d3ff2
Revises: 35d24e81eb53
Create Date: 2021-07-16 11:41:22.161127

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0fb6bd0d3ff2'
down_revision = '35d24e81eb53'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product_purchase_order', sa.Column('quantity', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product_purchase_order', 'quantity')
    # ### end Alembic commands ###
