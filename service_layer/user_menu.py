"""The User Menu Module."""
import copy
import sys
from typing import Tuple, List

from constants.constant_strings import ConstantStrings
from helpers import UserText
from service_layer.products import Product, LimitedProduct, NonStockedProduct
from service_layer.store import Store


class UserMenu:
    """Class to handel User Menu Operations."""
    __store: Store
    __menu_options = {}

    @classmethod
    def get_store(cls):
        """Method to Get the Store object."""
        return cls.__store

    @classmethod
    def set_store(cls, store: Store):
        """Method to Set the Store object."""
        try:
            if not isinstance(store, Store):
                raise ValueError
            cls.__store = store
        except ValueError as e:
            UserText.print_error(ConstantStrings.
                                 EXCEPTION_STRING.format(field="Store", exception=e))
            raise

    @classmethod
    def display_menu(cls):
        """Displays the menu and handles user input."""
        cls.__set_menu_options()  # Init Menu List
        while True:
            UserText.print_bold(ConstantStrings.MENU_HEADER)
            UserText.print_blue("\t__________")
            for key, (description, _) in cls.__menu_options.items():
                UserText.print_teal(f"{key}. {description}")

            try:
                choice = int(UserText.input_prompt(ConstantStrings.MENU_OPT_PROMPT).strip())
            except ValueError as e:
                print(ConstantStrings.MENU_OPT_INVALID)
                continue

            try:
                if choice in cls.__menu_options:
                    cls.__menu_options[choice][1]()
                else:
                    raise ValueError

            except ValueError:
                UserText.print_error(ConstantStrings.MENU_OPT_INVALID)

    @classmethod
    def list_products(cls) -> List[Tuple[int, Product]]:
        """Lists all products in store. And also returns List[Tuple[int, Product]]"""
        indexed_product_list = list(enumerate(cls.__store.get_all_products(), start=1))
        UserText.print_bold(ConstantStrings.PRODUCT_LIST_HEADER)
        for x in indexed_product_list:
            # 1. MacBook Air M2, Price: $1450, Quantity: 100
            UserText.print_teal(f"{x[0]}. {x[1]}")
        UserText.print_bold(ConstantStrings.PRODUCT_LIST_FOOTER)

    @classmethod
    def show_total_amount(cls):
        """Displays the total amount in store."""
        UserText.print_success(ConstantStrings.
                               MENU_TOTAL_QUANTITY.
                               format(number=cls.__store.get_total_quantity()))

    @classmethod
    def quit_program(cls):
        """Exits the program."""
        sys.exit(0)  # With no error Terminates the program

    @classmethod
    def make_order(cls):
        """Handles the order process."""
        cls.list_products()
        indexed_product_list = list(enumerate(cls.__store.get_all_products(), start=1))
        # Preserving the state of Store object and if order is made only
        # and then only the Store object will be modified.
        indexed_product_list = copy.deepcopy(indexed_product_list)
        prd_len = len(indexed_product_list)

        if prd_len == 0:
            UserText.print_error(ConstantStrings.MAKE_ORDER_NO_PRODUCTS)
            return

        orders_list = []

        while True:
            product_item = cls.__select_product(indexed_product_list, prd_len)
            if not product_item:
                if len(orders_list) == 0:
                    UserText.print_error(ConstantStrings.MAKE_ORDER_CANCEL)
                break  # User wants to exit

            quantity = cls.__select_quantity(product_item)
            if quantity is None:
                continue  # User canceled quantity selection, go back to product selection

            UserText.print_success(ConstantStrings.MAKE_ORDER_PRODUCT_ADDED)
            price_promotion_tuple = product_item.buy(quantity)
            name_price_promotion_tuple = (product_item.name, quantity) + price_promotion_tuple
            orders_list.append(name_price_promotion_tuple)

        if len(orders_list) == 0:
            return  # User has not ordered Anything, go back to the Main Menu

        cls.__finalize_order(orders_list, indexed_product_list)

    @classmethod
    def __select_product(cls, indexed_product_list, prd_len):
        """Handles product selection."""
        while True:
            UserText.print_blue(ConstantStrings.MAKE_ORDER_FINISH)
            val = UserText.input_prompt(ConstantStrings.
                                        MAKE_ORDER_ADD_PRODUCT.format(prd_len=prd_len)).strip()
            if val == "":
                return None  # User wants to exit

            try:
                index = int(val)
            except ValueError as e:
                cls.__print_custom_error(e, ConstantStrings.
                                         MAKE_ORDER_ADD_PRODUCT_INDEX_ERROR.format(prd_len=prd_len))
                continue

            try:
                if not 1 <= index <= prd_len:
                    raise ValueError(ConstantStrings.
                                     MAKE_ORDER_ADD_PRODUCT_INDEX_ERROR.format(prd_len=prd_len))
                return indexed_product_list[index - 1][1]  # Return the selected Product object

            except ValueError as e:
                # print(constant.EXCEPTION_STRING.format(field="Product Selection", exception=e))
                cls.__print_custom_error(e, ConstantStrings.MAKE_ORDER_ADD_PRODUCT_ERROR)

    @classmethod
    def __select_quantity(cls, product_item):
        """Handles quantity selection for the chosen product."""
        if isinstance(product_item, LimitedProduct):
            max_amt = product_item.maximum
        elif isinstance(product_item, Product):
            max_amt = product_item.quantity
        else:
            max_amt = None  # NonStockedProduct

        if not isinstance(product_item, NonStockedProduct):
            if product_item.quantity == 0:
                # The Product is not in the Warehouse.
                UserText.print_teal(ConstantStrings.PRODUCT_NOT_AVAILABLE)
                return None

        while True:
            if max_amt is not None:
                val = UserText.input_prompt(ConstantStrings.
                                            MAKE_ORDER_SELECT_QUANTITY_WITH_MAX.
                                            format(max_amt=max_amt)).strip()
            else:
                val = UserText.input_prompt(ConstantStrings.
                                            MAKE_ORDER_SELECT_QUANTITY).strip()

            if val == "":
                return None  # User wants to cancel and reselect product

            try:
                amt = int(val)
            except ValueError as e:
                cls.__print_custom_error(e, ConstantStrings.MAKE_ORDER_ADD_PRODUCT_QUANTITY_NOT_A_NUMBER_ERROR)
                continue

            try:
                if amt < 0:
                    raise ValueError(ConstantStrings.MAKE_ORDER_INVALID_QUANTITY)

                if max_amt is not None and amt > max_amt:
                    raise ValueError(ConstantStrings.
                                     MAKE_ORDER_SELECT_QUANTITY_ERROR.format(max_amt=max_amt))
                return amt

            except ValueError as e:
                # print(constant.EXCEPTION_STRING.format(field="Product Amount", exception=e))
                cls.__print_custom_error(e, ConstantStrings.MAKE_ORDER_ADD_PRODUCT_ERROR)

    @classmethod
    def __finalize_order(cls, orders_list, indexed_product_list):
        """Finalizes the order by displaying the total and updating the store."""
        # Update the store object with the new product list
        # (product_item, (price, promotion))
        total_amt = sum(x[2] for x in orders_list)
        cls.__store = Store([x[1] for x in indexed_product_list])
        UserText.print_success(ConstantStrings.MAKE_ORDER_AMOUNT.format(total_amt=total_amt))
        UserText.print_bold("-----Detailed Order-----")
        for item in orders_list:
            out = f"{item[0]}, Quantity: {item[1]}, Price: ${item[2]: .2f}"
            if len(item) > 3:
                out += f", Promotion: {item[3]}"
            UserText.print_teal(out)

    @classmethod
    def __set_menu_options(cls):
        if cls.__menu_options:
            return
        # Dictionary mapping user choices to functions
        cls.__menu_options = {
            1: (ConstantStrings.MENU_OPT_1, cls.list_products),
            2: (ConstantStrings.MENU_OPT_2, cls.show_total_amount),
            3: (ConstantStrings.MENU_OPT_3, cls.make_order),
            4: (ConstantStrings.MENU_OPT_4, cls.quit_program)
        }

    @classmethod
    def __print_custom_error(cls, ex: Exception, default_error: str):
        """Method to print custom error string."""
        error = str(ex)
        if error.startswith("CE-"):
            error = error.replace("CE-", "")
            UserText.print_error(error)
        else:
            UserText.print_error(default_error)
