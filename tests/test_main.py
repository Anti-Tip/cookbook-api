from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_main():
    """Тест получения списка рецептов."""
    response = client.get("/recipes/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_recipe():
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


def test_get_nonexistent_recipe():
    """Тест получения несуществующего рецепта."""
    response = client.get("/recipes/9999")
    assert response.status_code == 404