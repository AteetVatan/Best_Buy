"""Test Module for product class."""
import pytest
from constants import ConstantStrings
from service_layer.products.product import Product


# Test Magic Methods
def test_greater_less_then_products():
    """Test valid purchases"""
    prod1 = Product("Phone1", price=1000, quantity=100)
    prod2 = Product("Phone2", price=2000, quantity=100)

    assert prod2 > prod1
    assert not prod2 < prod1


# Test Promotions
@pytest.mark.parametrize("quantity, expected_total, "
                         "expected_promotion ,test_promotions", [
                             (1, 1000, None, ("second_half_price",)),
                             (2, 1500, "second_half_price",
                              ("second_half_price",)),
                             (5, 4000, "second_half_price",
                              ("second_half_price", "third_one_free")),
                             (6, 4000, "third_one_free",
                              ("second_half_price", "third_one_free")),
                             (10, 7000, "third_one_free",
                              ("second_half_price", "third_one_free", "thirty_percent"))
                         ])
def test_product_buy_valid_promotions(valid_product, promotions, quantity,
                                      expected_total,
                                      expected_promotion, test_promotions):
    """Test valid purchases"""
    valid_product.multiple_promotion = tuple(promotions[x] for x in test_promotions)
    total_cost_tuple = valid_product.buy(quantity)
    applied_promotion = dict(enumerate(total_cost_tuple)).get(1, None)
    assert applied_promotion == expected_promotion
    assert total_cost_tuple[0] == expected_total


# --- Test Cases for ProductModel ---
def test_product_valid(valid_product):
    """Test valid product creation"""
    product = valid_product
    assert product.name == "Phone"
    assert product.price == 1000
    assert product.quantity == 100
    assert product.active is True
    product.quantity = 0
    assert product.active is False


def test_limited_product_valid(valid_limited_product):
    """Test valid product creation"""
    product = valid_limited_product
    assert product.name == "Phone"
    assert product.price == 1000
    assert product.quantity == 100
    assert product.maximum == 10
    assert product.active is True


def test_non_stocked_product_valid(valid_non_stocked_product):
    """Test valid product creation"""
    product = valid_non_stocked_product
    assert product.name == "Phone"
    assert product.price == 1000
    assert product.active is True


def test_product_with_promotion_valid(valid_product, promotions):
    """Test valid product creation"""
    product = valid_product
    product.multiple_promotion.promotions = promotions["second_half_price"]
    price_promotion_tuple = valid_product.buy(4)
    assert price_promotion_tuple[0] == 3000
    assert price_promotion_tuple[1] == "second_half_price"


def test_product_with_multiple_promotion_valid(valid_product, promotions):
    """Test valid product creation"""
    product = valid_product
    product.multiple_promotion.promotions = tuple(promotions.values())
    price_promotion_tuple = valid_product.buy(4)
    assert price_promotion_tuple[0] == 2800
    assert price_promotion_tuple[1] == "thirty_percent"


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


def test_product_buy_invalid_types(valid_product):
    """Test buying with invalid types"""
    with pytest.raises(ValueError, match=ConstantStrings.PRODUCT_QUANTITY_ERROR):
        valid_product.buy("five")  # String instead of int/float

    with pytest.raises(ValueError, match=ConstantStrings.PRODUCT_QUANTITY_ERROR):
        valid_product.buy(None)  # NoneType


@pytest.mark.parametrize("quantity, expected_remaining, expected_total", [
    (1, 99, 1000),
    (5, 95, 5000),
    (10, 90, 10000)
])
def test_product_buy_valid(valid_product, quantity, expected_remaining, expected_total):
    """Test valid purchases"""
    total_cost_tuple = valid_product.buy(quantity)
    assert valid_product.quantity == expected_remaining
    assert total_cost_tuple[0] == expected_total


@pytest.mark.parametrize("quantity, expected_exception, expected_message", [
    (-1, ValueError, ConstantStrings.PRODUCT_QUANTITY_ERROR),  # Negative quantity
    (101, ValueError, ConstantStrings.PRODUCT_QUANTITY_NOT_AVAILABLE),  # More than available
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
