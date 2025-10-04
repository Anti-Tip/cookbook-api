import pytest
from fastapi.testclient import TestClient


@pytest.mark.asyncio
async def test_read_main(test_db, client: TestClient):
    """Тест получения списка рецептов."""
    response = client.get("/recipes/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_create_recipe(test_db, client: TestClient):
    """Тест создания рецепта."""
    recipe_data = {
        "title": "Test Recipe",
        "cooking_time": 30,
        "ingredients": "test ingredients",
        "instructions": "test instructions",
    }
    response = client.post("/recipes/", json=recipe_data)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Recipe"
    assert "id" in data


@pytest.mark.asyncio
async def test_get_nonexistent_recipe(test_db, client: TestClient):
    """Тест получения несуществующего рецепта."""
    response = client.get("/recipes/9999")
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_create_and_get_recipe(test_db, client: TestClient):
    """Тест создания и получения рецепта."""
    recipe_data = {
        "title": "Test Recipe 2",
        "cooking_time": 25,
        "ingredients": "ingredient1, ingredient2",
        "instructions": "Step 1, Step 2",
    }
    create_response = client.post("/recipes/", json=recipe_data)
    assert create_response.status_code == 200
    created_recipe = create_response.json()

    get_response = client.get(f"/recipes/{created_recipe['id']}")
    assert get_response.status_code == 200
    retrieved_recipe = get_response.json()

    assert retrieved_recipe["title"] == "Test Recipe 2"
    assert retrieved_recipe["views"] == 1
