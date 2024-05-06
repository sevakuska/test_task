from re import findall

from core.services.base import BaseService
from core.repositories.data import DataRepository
from core.models.data import DataModel


class DataService(BaseService):
    def __init__(self, repository: DataRepository) -> None:
        self._repository = repository

    async def add_one(self, data: str) -> int:
        if len(data) != 8:
            raise ValueError('Blabla1')

        if data[:2] != '80':
            raise ValueError('Blabla2')

        if not (0 <= int(data[2:4], 16) <= 127):
            raise ValueError('Blabla3')

        return await self._repository.create(
            int(data[2:4], 16),
            float(int(data[4:], 16)),
            int(data[:2])
        )

    async def add_all(self, data: str) -> list[int]:
        pattern = r'80[0-7f][0-9a-f]{5}'
        matches = findall(pattern, data)
        if not matches:
            return []

        packs = [
            {
                'current_value_counter': int(match[2:4], 16),
                'pressure_value': float(int(match[4:], 16)),
                'status': int(match[:2])
            }
            for match in matches
        ]

        return await self._repository.create_all(packs)

    async def get_one(self, id: int) -> DataModel:
        return await self._repository.read(id)

    async def get_all(self) -> list[DataModel]:
        return await self._repository.read_all()
