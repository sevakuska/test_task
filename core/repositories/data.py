from abc import abstractmethod

from core.models.data import DataModel
from core.repositories.base import BaseRepository


class DataRepository(BaseRepository):
    @abstractmethod
    async def create(
        self,
        current_value_counter: int,
        pressure_value: float,
        status: int
    ) -> int:
        ...

    @abstractmethod
    async def create_all(
        self,
        data: list[dict[str, int | float]]
    ) -> list[int]:
        ...

    @abstractmethod
    async def read(self, id: int) -> DataModel:
        ...

    @abstractmethod
    async def read_all(self) -> list[DataModel]:
        ...
