from flask import Flask
from flask.testing import FlaskClient
import pytest

@pytest.fixture
def client():
    app = Flask(__name__)
    client = app.test_client()
    return client

def test_list_all_products(client: FlaskClient):
    response = client.get("/products")
    assert response.status_code == 200

def test_read_product(client: FlaskClient):
    response = client.get("/products/1")
    assert response.status_code == 200

def test_update_product(client: FlaskClient):
    response = client.put("/products/1", json={"price": 899.99})
    assert response.status_code == 200

def test_delete_product(client: FlaskClient):
    response = client.delete("/products/1")
    assert response.status_code == 204

def test_list_by_name(client: FlaskClient):
    response = client.get("/products?name=Laptop")
    assert response.status_code == 200

def test_list_by_category(client: FlaskClient):
    response = client.get("/products?category=Electronics")
    assert response.status_code == 200

def test_list_by_availability(client: FlaskClient):
    response = client.get("/products?availability=true")
    assert response.status_code == 200
