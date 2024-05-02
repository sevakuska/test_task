from fastapi import FastAPI

from core.servs.data import DataServ


app = FastAPI()


@app.post('/data')
async def post_data(data: str) -> None:
    serv = DataServ()
    await serv.add_data(data)


@app.get('/data')
async def get_data() -> None:
    serv = DataServ()
    data = await serv.get_data()
    return [
        (
            i.current_value_counter,
            i.pressure_value,
            i.status,
        )
        for i in data
    ]
