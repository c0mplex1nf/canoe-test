"""Create Database

Revision ID: 6e1f83cbd25e
Revises: 
Create Date: 2023-12-04 13:26:30.757284

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e1f83cbd25e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('company',
    sa.Column('id', sa.String(length=255), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('log',
    sa.Column('id', sa.String(length=255), nullable=False),
    sa.Column('data', sa.JSON(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', 'data')
    )
    op.create_table('manager',
    sa.Column('id', sa.String(length=255), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('fund',
    sa.Column('id', sa.String(length=255), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('start_year', sa.String(length=255), nullable=True),
    sa.Column('nationality', sa.String(length=255), nullable=True),
    sa.Column('alias', sa.String(length=255), nullable=True),
    sa.Column('manager_id', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['manager_id'], ['manager.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('company_fund',
    sa.Column('company_id', sa.String(length=255), nullable=True),
    sa.Column('fund_id', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ),
    sa.ForeignKeyConstraint(['fund_id'], ['fund.id'], )
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('company_fund')
    op.drop_table('fund')
    op.drop_table('manager')
    op.drop_table('log')
    op.drop_table('company')
    # ### end Alembic commands ###
