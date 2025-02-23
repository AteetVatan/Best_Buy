"""Test Module for Store class."""
from service_layer import Product, Store


# Magic Methods
def test_product_in_stores():
    """Test product in store."""
    p1 = Product("MacBook Air M2", price=1450, quantity=100)
    p2 = Product("Bose QuietComfort Earbuds", price=250, quantity=500)

    store1 = Store([p1, p2])
    assert p1 in store1
    assert p2 in store1


def test_add_stores():
    """Test Add stores."""
    p1 = Product("MacBook Air M2", price=1450, quantity=100)
    p2 = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    p3 = Product("Google Pixel 7", price=500, quantity=250)
    p4 = Product("Mac pro Notebook", price=800, quantity=100)

    store1 = Store([p1, p2])
    store2 = Store([p3, p4])
    store3 = store1 + store2

    assert isinstance(store3, Store)
    assert len(store3.products) == len(store1.products) + len(store2.products)
    assert p1 in store3
    assert p3 in store3
