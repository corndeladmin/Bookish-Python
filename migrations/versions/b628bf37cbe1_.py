"""empty message

Revision ID: b628bf37cbe1
Revises: 
Create Date: 2023-02-10 14:13:15.807618

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b628bf37cbe1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    book_table = op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )

    # initial seed data
    op.bulk_insert(book_table,
                   [
                       {'id': 1, 'title': 'Wuthering Heights'},
                       {'id': 2, 'title': 'Jane Eyre'}
                   ])


def downgrade():
    op.drop_table('book')
