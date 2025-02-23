"""The Main Module."""
from service_layer import SecondHalfPrice, ThirdOneFree, PercentDiscount
from service_layer.products import Product, NonStockedProduct, LimitedProduct
from service_layer import Store
from service_layer import UserMenu


def start_best_buy():
    """Starts the Best Buy application."""
    store = initialize_store()
    user_operation(store)


def initialize_store() -> Store:
    """Set up Store object with setup initial stock of inventory."""
    product_list = load_products()
    apply_promotions(product_list)
    return Store(product_list)


def load_products():
    """Method to load products."""
    return [Product("MacBook Air M2", price=1450, quantity=100),
            Product("Bose QuietComfort Earbuds", price=250, quantity=500),
            Product("Google Pixel 7", price=500, quantity=250),
            Product("Mac pro Notebook", price=800, quantity=100),
            NonStockedProduct("Windows 11 License", price=125),
            NonStockedProduct("McAfee Antivirus License", price=50),
            LimitedProduct("Super Protein", price=10, quantity=250, maximum=5),
            LimitedProduct("Python Snake", price=1000, quantity=10, maximum=1)
            ]


def apply_promotions(product_list):
    """Function applying Promotions."""
    # Initialize Promotions
    second_half_price = SecondHalfPrice("Second Half price!")
    third_one_free = ThirdOneFree("Third One Free!")
    thirty_percent = PercentDiscount("30% off!", percent=30)

    # Add promotions to product
    product_list[1].multiple_promotion = third_one_free
    product_list[2].multiple_promotion = second_half_price, third_one_free
    product_list[3].multiple_promotion = second_half_price, third_one_free, thirty_percent
    # Add promotions to NonStockedProduct
    product_list[5].multiple_promotion = second_half_price, thirty_percent
    # Add promotions to LimitedProduct
    product_list[7].multiple_promotion = thirty_percent


def user_operation(store: Store):
    """Starts User Operation by displaying the Menu."""
    UserMenu.set_store(store)
    UserMenu.display_menu()


if __name__ == "__main__":
    start_best_buy()
