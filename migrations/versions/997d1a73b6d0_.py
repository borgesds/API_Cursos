"""empty message

Revision ID: 997d1a73b6d0
Revises: 
Create Date: 2023-10-23 18:59:28.548813

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '997d1a73b6d0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('curso',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('descricao', sa.String(length=100), nullable=False),
    sa.Column('data_publicacao', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('formacao',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('descricao', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('task')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('task',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('card', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('data_aberto', sa.DATE(), nullable=True),
    sa.Column('data_init_trab', sa.DATE(), nullable=True),
    sa.Column('resp_teste', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('data_teste', sa.DATE(), nullable=True),
    sa.Column('data_validacao', sa.DATE(), nullable=True),
    sa.Column('data_concluido', sa.DATE(), nullable=True),
    sa.Column('horas_trab', mysql.VARCHAR(length=5), nullable=True),
    sa.Column('link_card', mysql.VARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('formacao')
    op.drop_table('curso')
    # ### end Alembic commands ###