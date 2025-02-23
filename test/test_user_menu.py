"""The User Menu Test Module."""
from unittest.mock import patch
import pytest
from constants.constant_strings import ConstantStrings
from service_layer.user_menu import UserMenu
from service_layer.store import Store
from service_layer.products.product import Product


@pytest.fixture(autouse=True)
def setup_store():
    """Set up the real store for all test cases."""
    store = Store([
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250)
    ])
    UserMenu.set_store(store)


def test_validate_user_menu_methods():
    """Test that UserMenu has required methods and they are callable."""
    assert hasattr(UserMenu, "display_menu")
    assert callable(UserMenu.display_menu)
    assert hasattr(UserMenu, "make_order")
    assert callable(UserMenu.make_order)
    assert hasattr(UserMenu, "list_products")
    assert callable(UserMenu.list_products)
    assert hasattr(UserMenu, "show_total_amount")
    assert callable(UserMenu.show_total_amount)
    assert hasattr(UserMenu, "quit_program")
    assert callable(UserMenu.quit_program)


@patch("builtins.print")
def test_display_menu(mock_print):
    """Test menu display and exit."""
    with patch("builtins.input", side_effect=["4"]):
        with pytest.raises(SystemExit):
            UserMenu.display_menu()

    assert any(ConstantStrings.MENU_HEADER in call.args[0] for call in mock_print.call_args_list)
    # mock_print.assert_any_call(UserText.print_bold(ConstantStrings.MENU_HEADER))


@patch("builtins.print")
def test_dummy_order_and_store_quantity(mock_print):
    """Test making an order and checking store quantity."""
    initial_stock = UserMenu.get_store().get_total_quantity()

    with patch("builtins.input", side_effect=["2", "100", "", ""]):
        UserMenu.make_order()

    expected_stock = initial_stock - 100
    assert UserMenu.get_store().get_total_quantity() == expected_stock, \
        "Store quantity should be updated after order"
    assert any(ConstantStrings.MAKE_ORDER_PRODUCT_ADDED
               in call.args[0] for call in mock_print.call_args_list)
    # mock_print.assert_any_call(ConstantStrings.MAKE_ORDER_PRODUCT_ADDED)


@patch("builtins.print")
def test_order_cancellation_restores_store(mock_print):
    """Test if order cancellation restores store quantity."""
    initial_quantity = UserMenu.get_store().get_total_quantity()
    with patch("builtins.input", side_effect=["1", "", ""]):  # Cancelling after selecting product
        UserMenu.make_order()

    assert UserMenu.get_store().get_total_quantity() == initial_quantity, \
        "Store quantity should be restored after order cancellation"
    assert any(ConstantStrings.MAKE_ORDER_CANCEL
               in call.args[0] for call in mock_print.call_args_list)
    # mock_print.assert_any_call(ConstantStrings.MAKE_ORDER_CANCEL)


@patch("builtins.print")
def test_order_exceeding_stock(mock_print):
    """Test ordering a quantity exceeding stock availability."""
    with patch("builtins.input", side_effect=["2", "999", "", ""]):
        UserMenu.make_order()

    # mock_print.assert_any_call(ConstantStrings.
    #                            MAKE_ORDER_SELECT_QUANTITY_ERROR.
    #                            replace("CE-", "").format(max_amt=500))

    assert any(ConstantStrings.
               MAKE_ORDER_SELECT_QUANTITY_ERROR.
               replace("CE-", "").format(max_amt=500)
               in call.args[0] for call in mock_print.call_args_list)

    assert UserMenu.get_store().get_total_quantity() == 850, \
        "Store quantity should remain unchanged when order exceeds stock"


@patch("builtins.print")
def test_invalid_menu_choice(mock_print):
    """Test handling of invalid menu input."""
    with patch("builtins.input", side_effect=["", "invalid_text", "999", "-2", "5.2", "4"]):
        with pytest.raises(SystemExit):
            UserMenu.display_menu()

    assert any(ConstantStrings.MENU_OPT_INVALID
               in call.args[0] for call in mock_print.call_args_list)
    # mock_print.assert_any_call(ConstantStrings.MENU_OPT_INVALID)


@patch("builtins.print")
def test_list_products(mock_print):
    """Test listing products."""
    UserMenu.list_products()
    assert any(ConstantStrings.PRODUCT_LIST_HEADER
               in call.args[0] for call in mock_print.call_args_list)
    # mock_print.assert_any_call(ConstantStrings.PRODUCT_LIST_HEADER)
    products = UserMenu.get_store().products
    assert any(str(products[0]) in call.args[0] for call in mock_print.call_args_list)
    # mock_print.assert_any_call("1. MacBook Air M2, Price: $1450, Quantity: 100")
    assert any(str(products[1]) in call.args[0] for call in mock_print.call_args_list)
    # mock_print.assert_any_call("2. Bose QuietComfort Earbuds, Price: $250, Quantity: 500")
    assert any(str(products[2]) in call.args[0] for call in mock_print.call_args_list)
    # mock_print.assert_any_call("3. Google Pixel 7, Price: $500, Quantity: 250")
    assert any(ConstantStrings.PRODUCT_LIST_FOOTER
               in call.args[0] for call in mock_print.call_args_list)
    # mock_print.assert_any_call(ConstantStrings.PRODUCT_LIST_FOOTER)


@patch("builtins.print")
def test_make_order_invalid_product(mock_print):
    """Test invalid product selection in an order process."""
    with patch("builtins.input", side_effect=["999", ""]):
        UserMenu.make_order()

    prd_len = len(UserMenu.get_store().get_all_products())
    assert any(ConstantStrings.MAKE_ORDER_CANCEL
               in call.args[0] for call in mock_print.call_args_list)
    # mock_print.assert_any_call(ConstantStrings.MAKE_ORDER_CANCEL)
    assert any(ConstantStrings.MAKE_ORDER_ADD_PRODUCT_INDEX_ERROR.
               replace("CE-", "").format(prd_len=prd_len)
               in call.args[0] for call in mock_print.call_args_list)
    # mock_print.assert_any_call(
    #     ConstantStrings.MAKE_ORDER_ADD_PRODUCT_INDEX_ERROR.
    #     replace("CE-", "").format(prd_len=prd_len))


@patch("builtins.print")
def test_exit_during_order(mock_print):
    """Test user exiting order process without selecting a product."""
    with patch("builtins.input", side_effect=[""]):
        UserMenu.make_order()

    assert any(ConstantStrings.MAKE_ORDER_CANCEL
               in call.args[0] for call in mock_print.call_args_list)
    # mock_print.assert_any_call(ConstantStrings.MAKE_ORDER_CANCEL)
    assert UserMenu.get_store().get_total_quantity() == 850
