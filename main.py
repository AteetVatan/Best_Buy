"""The Main Module."""
from service_layer.product import Product
from service_layer.store import Store
from service_layer.user_menu import UserMenu


def start_best_buy():
    """Starts the Best Buy application."""
    store = init_store()
    user_operation(store)


def init_store() -> Store:
    """Set up Store object with setup initial stock of inventory."""
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250)
                    ]
    return Store(product_list)


def user_operation(store: Store):
    """Starts User Operation by displaying the Menu."""
    UserMenu.set_store(store)
    UserMenu.display_menu()


if __name__ == "__main__":
    start_best_buy()
