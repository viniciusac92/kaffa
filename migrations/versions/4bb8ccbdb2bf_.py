"""empty message

Revision ID: 4bb8ccbdb2bf
Revises: 3f6640208026
Create Date: 2021-07-19 12:06:36.225103

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4bb8ccbdb2bf'
down_revision = '3f6640208026'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cashiers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('initial_value', sa.Float(), nullable=True),
    sa.Column('balance', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('payment_method',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('stock', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('provider',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('trading_name', sa.String(length=200), nullable=False),
    sa.Column('cnpj', sa.String(length=18), nullable=False),
    sa.Column('phone', sa.String(length=12), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cnpj'),
    sa.UniqueConstraint('phone')
    )
    op.create_table('tables',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('number')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('type', sa.Integer(), nullable=False),
    sa.Column('password_hash', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('managers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('cpf', sa.String(length=11), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('id_user')
    )
    op.create_table('operators',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('cpf', sa.String(length=11), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('id_user')
    )
    op.create_table('provider_product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_product', sa.Integer(), nullable=False),
    sa.Column('id_provider', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_product'], ['products.id'], ),
    sa.ForeignKeyConstraint(['id_provider'], ['provider.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('waiters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('cpf', sa.String(length=11), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('id_user')
    )
    op.create_table('accounts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('id_cashier', sa.Integer(), nullable=False),
    sa.Column('id_waiter', sa.Integer(), nullable=False),
    sa.Column('id_table', sa.Integer(), nullable=False),
    sa.Column('id_payment_method', sa.Integer(), nullable=False),
    sa.Column('is_finished', sa.Boolean(), nullable=True),
    sa.Column('total_value', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['id_cashier'], ['cashiers.id'], ),
    sa.ForeignKeyConstraint(['id_payment_method'], ['payment_method.id'], ),
    sa.ForeignKeyConstraint(['id_table'], ['tables.id'], ),
    sa.ForeignKeyConstraint(['id_waiter'], ['waiters.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('operator_cashier',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_operator', sa.Integer(), nullable=False),
    sa.Column('id_cashier', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_cashier'], ['cashiers.id'], ),
    sa.ForeignKeyConstraint(['id_operator'], ['operators.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('purchase_order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_manager', sa.Integer(), nullable=False),
    sa.Column('id_provider', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('is_finished', sa.Boolean(), nullable=True),
    sa.Column('total_value', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['id_manager'], ['managers.id'], ),
    sa.ForeignKeyConstraint(['id_provider'], ['provider.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('account_product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_account', sa.Integer(), nullable=False),
    sa.Column('id_product', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_account'], ['accounts.id'], ),
    sa.ForeignKeyConstraint(['id_product'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_purchase_order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_order', sa.Integer(), nullable=False),
    sa.Column('id_product', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('cost', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['id_order'], ['purchase_order.id'], ),
    sa.ForeignKeyConstraint(['id_product'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product_purchase_order')
    op.drop_table('account_product')
    op.drop_table('purchase_order')
    op.drop_table('operator_cashier')
    op.drop_table('accounts')
    op.drop_table('waiters')
    op.drop_table('provider_product')
    op.drop_table('operators')
    op.drop_table('managers')
    op.drop_table('user')
    op.drop_table('tables')
    op.drop_table('provider')
    op.drop_table('products')
    op.drop_table('payment_method')
    op.drop_table('cashiers')
    # ### end Alembic commands ###
