from serviceLayer.products import Product
from serviceLayer.store import Store
from serviceLayer.user_menu import UserMenu


def init_best_buy():
    store = init_store()
    user_operation(store)


def init_store() -> Store:
    # setup initial stock of inventory
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250)
                    ]
    return Store(product_list)


def user_operation(store: Store):
    UserMenu.set_store(store)
    UserMenu.display_menu()


if __name__ == "__main__":
    init_best_buy()
