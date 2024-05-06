from fastapi import FastAPI

from core.models.data import DataModel
from core.services.data import DataService
from infra.impls.psql.repositories.data import PSQLDataRepository


app = FastAPI()


@app.post('/data')
async def add_data(data: str, all: bool = True) -> int | list[int]:
    data_service = DataService(PSQLDataRepository())

    if all:
        return await data_service.add_all(data)

    return await data_service.add_one(data)


@app.get('/data/{id}')
async def get_data_by_id(id: int) -> DataModel:
    data_service = DataService(PSQLDataRepository())

    data = await data_service.get_one(id)

    return data


@app.get('/data')
async def get_all_data() -> list[DataModel]:
    data_service = DataService(PSQLDataRepository())

    data = await data_service.get_all()

    return data
