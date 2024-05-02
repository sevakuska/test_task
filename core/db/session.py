from os import environ

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession

engine = create_async_engine(
    environ['DB_DSN'],
    echo=False
)
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False
)


async def get_database_session() -> AsyncSession:
    return AsyncSessionLocal()
