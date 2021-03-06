"""add user profile

Revision ID: 1237bc28d6fa
Revises: f8374be84c67
Create Date: 2016-03-14 11:37:45.104197

"""

# revision identifiers, used by Alembic.
revision = '1237bc28d6fa'
down_revision = 'f8374be84c67'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('about_me', sa.Text(), nullable=True))
    op.add_column('users', sa.Column('signature', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'signature')
    op.drop_column('users', 'about_me')
    ### end Alembic commands ###
