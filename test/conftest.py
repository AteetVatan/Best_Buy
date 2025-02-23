"""common Pytest Fixture Module for test_product module"""
import pytest

from service_layer import LimitedProduct, NonStockedProduct, SecondHalfPrice, ThirdOneFree, PercentDiscount
from service_layer.products.product import Product


@pytest.fixture
def valid_product():
    """Test valid product creation"""
    return Product("Phone", price=1000, quantity=100)


@pytest.fixture
def valid_limited_product():
    """Test valid product creation"""
    return LimitedProduct("Phone", price=1000, quantity=100, maximum=10)


@pytest.fixture
def valid_non_stocked_product():
    """Test valid product creation"""
    return NonStockedProduct("Phone", price=1000)


@pytest.fixture(scope="function")
def zero_quantity_product():
    """Create a product with zero quantity"""
    return Product("OutOfStock", 1000, quantity=0)

@pytest.fixture
def promotions():
    return{
    "second_half_price" : SecondHalfPrice("second_half_price"),
    "third_one_free" : ThirdOneFree("third_one_free"),
    "thirty_percent" : PercentDiscount("thirty_percent", percent=30),
    }