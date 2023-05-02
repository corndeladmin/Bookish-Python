"""empty message

Revision ID: cd0fba16d40c
Revises: b628bf37cbe1
Create Date: 2023-05-02 15:07:00.712472

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'cd0fba16d40c'
down_revision = 'b628bf37cbe1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books')
    op.drop_table('SequelizeMeta')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('SequelizeMeta',
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('name', name='SequelizeMeta_pkey')
    )
    op.create_table('books',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('createdAt', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('updatedAt', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='books_pkey')
    )
    # ### end Alembic commands ###