import os
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Используем test базу для тестов
if os.getenv("TESTING"):
    DATABASE_URL = "sqlite+aiosqlite:///./test_cookbook.db"
else:
    DATABASE_URL = "sqlite+aiosqlite:///./cookbook.db"

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(engine,
                             expire_on_commit=False,
                             class_=AsyncSession
                             )  # type: ignore
Base = declarative_base()


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session
