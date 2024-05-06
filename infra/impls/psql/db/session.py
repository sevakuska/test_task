from os import environ

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession


env_credential_names = (
    'DATABASE_DRIVER',
    'DATABASE_API',
    'DATABASE_USER',
    'DATABASE_PASSWORD',
    'DATABASE_HOST',
    'DATABASE_PORT',
    'DATABASE_NAME'
)
URL = '{}+{}://{}:{}@{}:{}/{}'.format(
    *(environ[env_var] for env_var in env_credential_names)
)
engine = create_async_engine(URL, echo=False)
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False
)


async def get_database_session() -> AsyncSession:
    return AsyncSessionLocal()
