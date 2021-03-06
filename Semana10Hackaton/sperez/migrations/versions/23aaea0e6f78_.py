"""empty message

Revision ID: 23aaea0e6f78
Revises: 
Create Date: 2020-08-09 18:55:11.860506

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '23aaea0e6f78'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tipo_documento',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('descripcion', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tipo_documento_descripcion'), 'tipo_documento', ['descripcion'], unique=False)
    op.create_table('cliente',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('documento', sa.Integer(), nullable=True),
    sa.Column('numero_documento', sa.String(length=10), nullable=True),
    sa.Column('nombre', sa.String(length=50), nullable=True),
    sa.Column('apellido_pat', sa.String(length=50), nullable=True),
    sa.Column('apellido_mat', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['documento'], ['tipo_documento.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('factura',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cliente', sa.Integer(), nullable=True),
    sa.Column('fecha', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['cliente'], ['cliente.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_factura_fecha'), 'factura', ['fecha'], unique=False)
    op.create_table('detalle_factura',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('factura', sa.Integer(), nullable=True),
    sa.Column('producto', sa.Integer(), nullable=True),
    sa.Column('cantidad', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['factura'], ['factura.id'], ),
    sa.ForeignKeyConstraint(['producto'], ['producto.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index('ix_post_timestamp', table_name='post')
    op.drop_table('post')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('body', sa.VARCHAR(length=140), autoincrement=False, nullable=True),
    sa.Column('timestamp', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='post_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='post_pkey')
    )
    op.create_index('ix_post_timestamp', 'post', ['timestamp'], unique=False)
    op.drop_table('detalle_factura')
    op.drop_index(op.f('ix_factura_fecha'), table_name='factura')
    op.drop_table('factura')
    op.drop_table('cliente')
    op.drop_index(op.f('ix_tipo_documento_descripcion'), table_name='tipo_documento')
    op.drop_table('tipo_documento')
    # ### end Alembic commands ###
