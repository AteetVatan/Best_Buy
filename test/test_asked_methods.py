"""Module to test the asked project Functionality"""
import pytest
from constants import ConstantStrings
from service_layer import products, store


def test_asked_method():
    """Function to test the asked project Functionality"""
    # setup initial stock of inventory
    mac = products.Product("MacBook Air M2", price=1450, quantity=100)
    bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    pixel = products.Product("Google Pixel 7", price=500, quantity=250, maximum=1)

    best_buy = store.Store([mac, bose])

    with pytest.raises(ValueError, match=ConstantStrings.PRODUCT_PRICE_ERROR):
        mac.price = -100  # Should give error ConstantStrings.PRODUCT_PRICE_ERROR

    # Should print "MacBook Air M2, Price: $1450, Quantity: 100"
    assert str(mac) == "MacBook Air M2, Price: $1450, Quantity: 100"
    assert mac > bose  # Should print True
    assert mac in best_buy  # Should print True
    assert not pixel in best_buy  # Should print False
