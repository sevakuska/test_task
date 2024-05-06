from typing import Sequence

from alembic.op import create_table
from alembic.op import create_index
from alembic.op import drop_table
from alembic.op import drop_index
from alembic.op import f as F
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import PrimaryKeyConstraint


revision: str = 'b34b66d2fe7d'
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    create_table(
        'data_table',
        Column('id', Integer(), nullable=False),
        Column('current_value_counter', Integer(), nullable=False),
        Column('pressure_value', Float(), nullable=False),
        Column('status', Integer(), nullable=False),
        PrimaryKeyConstraint('id')
    )
    create_index(F('ix_data_table_id'), 'data_table', ['id'], unique=False)


def downgrade() -> None:
    drop_index(F('ix_data_table_id'), table_name='data_table')
    drop_table('data_table')
