from dataclasses import dataclass

from core.models.base import BaseModel


@dataclass(frozen=True, slots=True)
class DataModel(BaseModel):
    id: int
    current_value_counter: int
    pressure_value: float
    status: int
