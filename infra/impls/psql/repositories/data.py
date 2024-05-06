from sqlalchemy import select

from core.models.data import DataModel
from core.repositories.data import DataRepository
from core.exceptions.not_found import NotFoundException
from core.exceptions.unknown import UnknownException
from infra.impls.psql.entities.data import DataEntity
from infra.impls.psql.db.session import get_database_session


class PSQLDataRepository(DataRepository):
    async def create(
        self,
        current_value_counter: int,
        pressure_value: float,
        status: int
    ) -> int:
        try:
            session = await get_database_session()

            data = DataEntity(
                current_value_counter=current_value_counter,
                pressure_value=pressure_value,
                status=status
            )
            session.add(data)
            await session.commit()

            return data.id
        except Exception as exception:
            await session.rollback()
            raise UnknownException(*exception.args)
        finally:
            await session.close()

    async def create_all(
        self,
        data: list[dict[str, int | float]]
    ) -> list[int]:
        try:
            session = await get_database_session()

            list_data = [
                DataEntity(
                    current_value_counter=i['current_value_counter'],
                    pressure_value=i['pressure_value'],
                    status=i['status']
                )
                for i in data
            ]
            session.add_all(list_data)
            await session.commit()

            return [i.id for i in list_data]
        except Exception as exception:
            await session.rollback()
            raise UnknownException(*exception.args)
        finally:
            await session.close()

    async def read(self, id: int) -> DataModel:
        try:
            session = await get_database_session()
            data = await session.get(DataEntity, id)

            if data is None:
                raise NotFoundException

            return DataModel(
                data.id,
                data.current_value_counter,
                data.pressure_value,
                data.status
            )
        except NotFoundException:
            await session.rollback()
            raise NotFoundException('Data not found by id.')
        except Exception as exception:
            await session.rollback()
            raise UnknownException(*exception.args)
        finally:
            await session.close()

    async def read_all(self) -> list[DataModel]:
        try:
            session = await get_database_session()
            query = select(DataEntity)
            query_result = await session.execute(query)

            return [
                DataModel(
                    id=i.id,
                    current_value_counter=i.current_value_counter,
                    pressure_value=i.pressure_value,
                    status=i.status
                )
                for i in query_result.scalars()
            ]
        except Exception as exception:
            await session.rollback()
            raise UnknownException(*exception.args)
        finally:
            await session.close()
