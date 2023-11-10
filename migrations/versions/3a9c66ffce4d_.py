"""empty message

Revision ID: 3a9c66ffce4d
Revises: 818e5a264273
Create Date: 2023-11-09 07:08:13.843229

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a9c66ffce4d'
down_revision = '818e5a264273'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('professor_formacao',
    sa.Column('professor_id', sa.Integer(), nullable=False),
    sa.Column('formacao_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['formacao_id'], ['formacao.id'], ),
    sa.ForeignKeyConstraint(['professor_id'], ['professor.id'], ),
    sa.PrimaryKeyConstraint('professor_id', 'formacao_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('professor_formacao')
    # ### end Alembic commands ###