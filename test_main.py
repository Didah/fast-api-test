from starlette.testclient import TestClient

from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_read_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_read_item():
    response = client.get("/items/0")
    assert response.status_code == 200
    result = response.json()
    assert result.get('name') == 'item 1'
    assert result.get('description') == 'description 1'
    assert result.get('price') == 123


def test_read_item_inexistent():
    response = client.get("/items/250")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}


def test_create_item():
    response = client.post(
        "/items/",
        json={"name": "blah", "description": "blah description", "price": 12})
    assert response.status_code == 200
    assert response.json() == {
        "description": "blah description",
        "name": "blah",
        "price": 12
    }
