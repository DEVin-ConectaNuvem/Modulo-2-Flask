"""empty message

Revision ID: 9051c8068a23
Revises: edb887b8a61c
Create Date: 2022-08-02 21:33:48.072125

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9051c8068a23'
down_revision = 'edb887b8a61c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('city_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=84), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=84), nullable=False),
    sa.Column('password', sa.String(length=84), nullable=False),
    sa.ForeignKeyConstraint(['city_id'], ['cities.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
