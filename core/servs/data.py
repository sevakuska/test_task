from re import findall

from core.repos.data import DataRepo
from core.servs.base import BaseServ
from core.models.data import DataModel


class DataServ(BaseServ):
    def __init__(self, repo_type: type[DataRepo] = None) -> None:
        self._repo = DataRepo() if repo_type is None else repo_type()

    async def add_data(self, data: str) -> None:
        pattern = r'80[0-7f][0-9a-f]{5}'
        matches = findall(pattern, data)
        if not matches:
            return

        serialized_packs = (
            {
                'status': int(match[:2]),
                'current_value_counter': int(match[2:4], 16),
                'pressure_value': float(int(match[4:], 16))
            }
            for match in matches
        )
        await self._repo.create(serialized_packs)

    async def get_data(self) -> list[DataModel]:
        return await self._repo.read_all()
