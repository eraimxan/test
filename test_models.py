import pytest
from models import Product

def test_read_product():
    product = Product(name="Laptop", category="Electronics", price=999.99, availability=True)
    assert product.name == "Laptop"

def test_update_product():
    product = Product(name="Laptop", category="Electronics", price=999.99, availability=True)
    product.price = 899.99
    assert product.price == 899.99

# Add similar tests for Delete, List All, Find by Name, Category, and Availability