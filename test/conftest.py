"""common Pytest Fixture Module for test_product module"""
import pytest
from service_layer.product import Product


@pytest.fixture
def valid_product():
    """Create a valid product instance"""
    return Product("Laptop", 1500, quantity=10)


@pytest.fixture(scope="function")
def zero_quantity_product():
    """Create a product with zero quantity"""
    return Product("OutOfStock", 1000, quantity=0)
