"""Added

Revision ID: b2e477b697da
Revises: 
Create Date: 2021-06-15 20:10:10.119622

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b2e477b697da'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employee',
    sa.Column('id', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=30), nullable=False),
    sa.Column('surname', mysql.VARCHAR(length=30), nullable=False),
    sa.Column('mid_name', mysql.VARCHAR(length=30), nullable=True),
    sa.Column('date_of_birth', sa.DATE(), nullable=False),
    sa.Column('salary', mysql.DECIMAL(precision=10, scale=0), nullable=False),
    sa.Column('related_department', mysql.VARCHAR(length=50), nullable=True),
    sa.ForeignKeyConstraint(['related_department'], ['department.id'], name='employee_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('id', 'employee', ['id'], unique=False)
    op.create_table('department',
    sa.Column('id', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('name', 'department', ['name'], unique=False)
    op.create_index('id', 'department', ['id'], unique=False)
    # ### end Alembic commands ###
