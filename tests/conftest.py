import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base, get_db
from app.main import app

TEST_DATABASE_URL = "sqlite+aiosqlite:///./test_cookbook.db"

test_engine = create_async_engine(TEST_DATABASE_URL, echo=False)
TestingSessionLocal = sessionmaker(
    test_engine, expire_on_commit=False, class_=AsyncSession
)


async def override_get_db():
    async with TestingSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()


@pytest.fixture(scope="function")
async def test_db():
    # Создаем таблицы
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # Заменяем зависимость
    app.dependency_overrides[get_db] = override_get_db

    yield

    # Удаляем таблицы после теста
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

    # Восстанавливаем оригинальную зависимость
    app.dependency_overrides.clear()


@pytest.fixture
def client():
    return TestClient(app)
