"""Renaming students to scholars

Revision ID: 99011341b331
Revises: 791279dd0760
Create Date: 2023-12-18 16:01:24.233389

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99011341b331'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')

def downgrade() -> None:
    op.rename_table('scholars', 'students')