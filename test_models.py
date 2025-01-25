import pytest
from models import Product

def test_read_product():
    product = Product(name="Laptop", category="Electronics", price=999.99, availability=True)
    assert product.name == "Laptop"

def test_update_product():
    product = Product(name="Laptop", category="Electronics", price=999.99, availability=True)
    product.price = 899.99
    assert product.price == 899.99

def test_delete_product():
    product = Product(name="Laptop", category="Electronics", price=999.99, availability=True)
    product.delete()
    assert product.id is None

def test_list_all_products():
    products = Product.list_all()
    assert len(products) > 0

def test_find_by_name():
    products = Product.find_by_name("Laptop")
    assert len(products) > 0

def test_find_by_category():
    products = Product.find_by_category("Electronics")
    assert len(products) > 0

def test_find_by_availability():
    products = Product.find_by_availability(True)
    assert len(products) > 0
