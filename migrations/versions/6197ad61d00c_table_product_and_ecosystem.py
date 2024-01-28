"""table product and ecosystem

Revision ID: 6197ad61d00c
Revises: 7c05f10113e1
Create Date: 2024-01-28 18:44:20.319723

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '6197ad61d00c'
down_revision = '7c05f10113e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('products',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=1000), nullable=False),
    sa.Column('images', sa.JSON(), nullable=False),
    sa.Column('brand', sa.String(length=100), nullable=False),
    sa.Column('sold', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_products_brand'), ['brand'], unique=False)
        batch_op.create_index(batch_op.f('ix_products_category_id'), ['category_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_products_name'), ['name'], unique=False)

    op.create_table('variants',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('image', sa.String(length=100), nullable=False),
    sa.Column('default_price', sa.Float(), nullable=False),
    sa.Column('sale_price', sa.Float(), nullable=False),
    sa.Column('option', sa.JSON(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('accounts', schema=None) as batch_op:
        batch_op.alter_column('role',
               existing_type=postgresql.ENUM('ADMIN', 'USER', name='account_role'),
               type_=sa.Enum('ADMIN', 'USER', name='account_role'),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('accounts', schema=None) as batch_op:
        batch_op.alter_column('role',
               existing_type=sa.Enum('ADMIN', 'USER', name='account_role'),
               type_=postgresql.ENUM('ADMIN', 'USER', name='account_role'),
               existing_nullable=False)

    op.drop_table('variants')
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_products_name'))
        batch_op.drop_index(batch_op.f('ix_products_category_id'))
        batch_op.drop_index(batch_op.f('ix_products_brand'))

    op.drop_table('products')
    op.drop_table('categories')
    # ### end Alembic commands ###
