import copy
import sys
from functools import total_ordering
from typing import Tuple, List

from constants import constant
from serviceLayer.store import Store
from serviceLayer.products import Product


class UserMenu:
    __store: Store
    __menu_options = {}

    @classmethod
    def get_store(cls):
        return cls.__store

    @classmethod
    def set_store(cls, store: Store):
        try:
            if not isinstance(store, Store):
                raise ValueError
            cls.__store = store
        except ValueError as e:
            print(constant.EXCEPTION_STRING.format(field="Store", exception=e))
            raise

    @classmethod
    def display_menu(cls):
        """Displays the menu and handles user input."""
        cls.__set_menu_options()  # Init Menu List
        while True:
            print(constant.MENU_HEADER)
            print("\t__________")
            for key, (description, _) in cls.__menu_options.items():
                print(f"{key}. {description}", )

            try:
                choice = int(float(input(constant.MENU_OPT_PROMPT).strip()))
                if choice in cls.__menu_options:
                    cls.__menu_options[choice][1]()
                else:
                    raise ValueError

            except ValueError:
                print(constant.MENU_OPT_INVALID)

    @classmethod
    def list_products(cls) -> List[Tuple[int, Product]]:
        """Lists all products in store. And also returns List[Tuple[int,Product]]"""
        indexed_product_list = list(enumerate(cls.__store.get_all_products(), start=1))
        print(constant.PRODUCT_LIST_HEADER)
        for x in indexed_product_list:
            # 1. MacBook Air M2, Price: $1450, Quantity: 100
            print(f"{x[0]}. {x[1].show()}")
        print(constant.PRODUCT_LIST_FOOTER)

    @classmethod
    def show_total_amount(cls):
        """Displays the total amount in store."""
        print(constant.MENU_TOTAL_QUANTITY.format(number=cls.__store.get_total_quantity()))

    @classmethod
    def quit_program(cls):
        """Exits the program."""
        sys.exit(0)  # With no error Terminates the program

    @classmethod
    def make_order(cls):
        """Handles the order process."""
        cls.list_products()
        indexed_product_list = list(enumerate(cls.__store.get_all_products(), start=1))
        # Preserving the state of Store object and if order will be made only
        # and then only the Store object will be modified.
        indexed_product_list = copy.deepcopy(indexed_product_list)
        prd_len = len(indexed_product_list)

        if prd_len == 0:
            print(constant.MAKE_ORDER_NO_PRODUCTS)
            return

        orders_cost_list = []

        while True:
            product_item = cls.__select_product(indexed_product_list, prd_len)
            if not product_item:
                if len(orders_cost_list) == 0:
                    print(constant.MAKE_ORDER_CANCEL)
                break  # User wants to exit

            quantity = cls.__select_quantity(product_item)
            if quantity is None:
                continue  # User canceled quantity selection, go back to product selection

            print(constant.MAKE_ORDER_PRODUCT_ADDED)
            orders_cost_list.append(product_item.buy(quantity))

        if len(orders_cost_list) == 0:
            return  # User has not ordered Anything, go back to Main Menu

        cls.__finalize_order(orders_cost_list, indexed_product_list)

    @classmethod
    def __select_product(cls, indexed_product_list, prd_len):
        """Handles product selection."""
        while True:
            print(constant.MAKE_ORDER_FINISH)
            val = input(constant.MAKE_ORDER_ADD_PRODUCT.format(prd_len=prd_len)).strip()
            if val == "":
                return None  # User wants to exit

            try:
                index = int(float(val))
                if not 1 <= index <= prd_len:
                    raise ValueError(constant.MAKE_ORDER_ADD_PRODUCT_INDEX_ERROR.format(prd_len=prd_len))
                return indexed_product_list[index - 1][1]  # Return the selected Product object

            except ValueError as e:
                # print(constant.EXCEPTION_STRING.format(field="Product Selection", exception=e))
                cls.__print_custom_error(e, constant.MAKE_ORDER_ADD_PRODUCT_ERROR)

    @classmethod
    def __select_quantity(cls, product_item):
        """Handles quantity selection for the chosen product."""
        max_amt = product_item.quantity
        while True:
            val = input(constant.MAKE_ORDER_SELECT_QUANTITY.format(max_amt=max_amt)).strip()

            if val == "":
                return None  # User wants to cancel and reselect product

            try:
                amt = float(val)
                if amt > max_amt:
                    raise ValueError(constant.MAKE_ORDER_SELECT_QUANTITY_ERROR.format(max_amt=max_amt))
                elif amt < 0:
                    raise ValueError(constant.MAKE_ORDER_INVALID_QUANTITY)
                return amt

            except ValueError as e:
                # print(constant.EXCEPTION_STRING.format(field="Product Amount", exception=e))
                cls.__print_custom_error(e, constant.MAKE_ORDER_ADD_PRODUCT_ERROR)

    @classmethod
    def __finalize_order(cls, orders_cost_list, indexed_product_list):
        """Finalizes the order by displaying the total and updating the store."""
        # Update the store object with the new product list
        total_amt = sum(orders_cost_list)
        cls.__store = Store([x[1] for x in indexed_product_list])
        print(constant.MAKE_ORDER_AMOUNT.format(total_amt=total_amt))

    @classmethod
    def __set_menu_options(cls):
        if cls.__menu_options:
            return
        # Dictionary mapping user choices to functions
        cls.__menu_options = {
            1: (constant.MENU_OPT_1, cls.list_products),
            2: (constant.MENU_OPT_2, cls.show_total_amount),
            3: (constant.MENU_OPT_3, cls.make_order),
            4: (constant.MENU_OPT_4, cls.quit_program)
        }

    @classmethod
    def __print_custom_error(cls, ex: Exception, default_error: str):
        """Method to print custom error string."""
        error = str(ex)
        if error.startswith("CE-"):
            error = error.replace("CE-", "")
            print(error)
        else:
            print(default_error)
