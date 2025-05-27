"""init

Revision ID: 0001
Revises: 
Create Date: 2025-05-27 00:00:00

"""
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String, unique=True, nullable=False),
        sa.Column('hashed_password', sa.String, nullable=False),
        sa.Column('full_name', sa.String),
        sa.Column('is_active', sa.Boolean, default=True),
        sa.Column('is_verified', sa.Boolean, default=False),
        sa.Column('role', sa.Enum('admin', 'user', name='roleenum'), default='user'),
    )
    # ... repeat for other tables (apis, api_requests, email_groups, emails, api_group_link, email_settings)

def downgrade():
    op.drop_table('users')
    # ... repeat for other tables