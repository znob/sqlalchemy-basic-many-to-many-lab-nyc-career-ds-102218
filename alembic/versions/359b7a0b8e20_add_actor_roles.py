"""add actor roles

Revision ID: 359b7a0b8e20
Revises:
Create Date: 2018-05-23 14:46:45.108214

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '359b7a0b8e20'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'actor_roles',
        sa.Column(
            'actor_id', sa.Integer,
            sa.ForeignKey('actors.id'), primary_key=True
        ),
        sa.Column(
            'role_id', sa.Integer,
            sa.ForeignKey('role.id'), primary_key=True
        )
    )


def downgrade():
    op.drop_table(
        'actor_roles'
    )
