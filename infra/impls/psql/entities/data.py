from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from infra.impls.psql.entities.base import BaseEntity


class DataEntity(BaseEntity):
    __tablename__ = 'data_table'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    current_value_counter: Mapped[int] = mapped_column(nullable=False)
    pressure_value: Mapped[float] = mapped_column(nullable=False)
    status: Mapped[int] = mapped_column(nullable=False)
