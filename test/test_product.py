"""Test Module for product class."""
import pytest
from constants import ConstantStrings
from service_layer.product import Product


# --- Test Cases for ProductModel ---
def test_product_valid():
    """Test valid product creation"""
    product = Product("Phone", 700, 5)
    assert product.name == "Phone"
    assert product.price == 700
    assert product.quantity == 5
    assert product.active is True


@pytest.mark.parametrize("name, price, quantity, expected_exception, expected_message", [
    ("", 100, 1, ValueError, ConstantStrings.PRODUCT_NAME_ERROR),  # Empty name
    (" ", 100, 1, ValueError, ConstantStrings.PRODUCT_NAME_ERROR),  # Empty name with space
    (None, 100, 1, ValueError, ConstantStrings.PRODUCT_NAME_ERROR),  # None name
    (123, 100, 1, ValueError, ConstantStrings.PRODUCT_NAME_ERROR)  # Integer as name
])
def test_product_model_invalid_name(name, price, quantity, expected_exception, expected_message):
    """Test invalid product name creation scenarios with multiple invalid cases"""
    with pytest.raises(expected_exception, match=expected_message):
        Product(name, price, quantity)


@pytest.mark.parametrize("name, price, quantity, expected_exception, expected_message", [
    ("Phone", -1, 1, ValueError, ConstantStrings.PRODUCT_PRICE_ERROR),  # Negative price
    ("Phone", "free", 1, ValueError, ConstantStrings.PRODUCT_PRICE_ERROR),  # String as price
    ("Phone", None, 1, ValueError, ConstantStrings.PRODUCT_PRICE_ERROR)  # None price
])
def test_product_model_invalid_price(name, price, quantity, expected_exception, expected_message):
    """Test invalid product price creation scenarios with multiple invalid cases"""
    with pytest.raises(expected_exception, match=expected_message):
        Product(name, price, quantity)


def test_product_buy_exact_quantity(valid_product):
    """Test that buying exact stock deactivates product"""
    total_cost = valid_product.buy(10)
    assert valid_product.quantity == 0
    assert total_cost == 15000
    assert valid_product.is_active() is False


def test_product_buy_invalid_types(valid_product):
    """Test buying with invalid types"""
    with pytest.raises(ValueError, match=ConstantStrings.PRODUCT_QUANTITY_ERROR):
        valid_product.buy("five")  # String instead of int/float

    with pytest.raises(ValueError, match=ConstantStrings.PRODUCT_QUANTITY_ERROR):
        valid_product.buy(None)  # NoneType


@pytest.mark.parametrize("quantity, expected_remaining, expected_total", [
    (1, 9, 1500),  # Buying 1 reduce stock to 9
    (5, 5, 7500),  # Buying 5 reduces stock to 5
    (10, 0, 15000)  # Buying all stock
])
def test_product_buy_valid(valid_product, quantity, expected_remaining, expected_total):
    """Test valid purchases"""
    total_cost = valid_product.buy(quantity)
    assert valid_product.quantity == expected_remaining
    assert total_cost == expected_total


def test_product_zero_quantity_behavior(zero_quantity_product):
    """Test behavior of a product that starts with zero quantity"""
    assert zero_quantity_product.quantity == 0
    assert zero_quantity_product.is_active() is False


@pytest.mark.parametrize("quantity, expected_exception, expected_message", [
    (-1, ValueError, ConstantStrings.PRODUCT_QUANTITY_ERROR),  # Negative quantity
    (11, ValueError, ConstantStrings.PRODUCT_QUANTITY_NOT_AVAILABLE),  # More than available
])
def test_product_buy_invalid(valid_product, quantity, expected_exception, expected_message):
    """Test invalid purchase scenarios"""
    with pytest.raises(expected_exception, match=expected_message):
        valid_product.buy(quantity)


@pytest.mark.parametrize("new_price", [0, 999, 2500])
def test_product_price_update(valid_product, new_price):
    """Test valid price updates"""
    valid_product.price = new_price
    assert valid_product.price == new_price


@pytest.mark.parametrize("invalid_price, expected_exception, expected_message", [
    (-1, ValueError, ConstantStrings.PRODUCT_PRICE_ERROR),  # Negative price
    ("expensive", ValueError, ConstantStrings.PRODUCT_PRICE_ERROR),  # String price
])
def test_product_invalid_price_update(valid_product,
                                      invalid_price,
                                      expected_exception,
                                      expected_message):
    """Test invalid price updates"""
    with pytest.raises(expected_exception, match=expected_message):
        valid_product.price = invalid_price


@pytest.mark.parametrize("invalid_quantity, expected_exception, expected_message", [
    (-5, ValueError, ConstantStrings.PRODUCT_QUANTITY_ERROR),  # Negative quantity
    ("many", ValueError, ConstantStrings.PRODUCT_QUANTITY_ERROR),  # Non-numeric
])
def test_product_invalid_quantity_update(valid_product,
                                         invalid_quantity,
                                         expected_exception,
                                         expected_message):
    """Test invalid quantity updates"""
    with pytest.raises(expected_exception, match=expected_message):
        valid_product.quantity = invalid_quantity
