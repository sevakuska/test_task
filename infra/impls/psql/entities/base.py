from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase


class BaseEntity(AsyncAttrs, DeclarativeBase):
    ...
