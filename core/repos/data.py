from sqlalchemy import select

from core.repos.base import BaseRepo
from core.models.data import DataModel
from core.db.session import get_database_session


class DataRepo(BaseRepo):
    async def create(self, data: list[dict[str, int | float]]) -> None:
        data_rows = (DataModel(**pack) for pack in data)

        try:
            session = await get_database_session()
            session.add_all(data_rows)
            await session.commit()
        finally:
            await session.close()

    async def read_all(self) -> None:
        try:
            session = await get_database_session()
            query = select(DataModel)
            return [i[0] for i in await session.execute(query)]
        finally:
            await session.close()
