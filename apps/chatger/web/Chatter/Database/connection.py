import os
from collections.abc import AsyncIterable

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.environ["DATABASE_URL"]

__all__ = ["engine", "get_db"]

engine = create_async_engine(DATABASE_URL, future=True, echo=True)
AsyncSessionFactory = sessionmaker(
    bind=engine, autoflush=False, expire_on_commit=False, class_=AsyncSession
)


async def get_db() -> AsyncIterable[AsyncSession]:
    async with AsyncSessionFactory() as session:
        yield session
