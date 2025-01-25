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

# Add tests for Read, Update, Delete, List by Name, Category, and Availability