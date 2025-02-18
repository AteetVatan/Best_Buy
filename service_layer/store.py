"""The Store Module."""
import copy
from typing import List, Tuple, Optional
from datetime import datetime
from constants.constant_strings import ConstantStrings
from service_layer.product import Product


class Store:
    """The Store Class to manage products."""

    __store_instances: List[Tuple[List[Product], str]] = []

    def __init__(self, products: Optional[List[Product]] = None):
        self.__products: List[Product] = products if products is not None else []
        formatted_time = datetime.now().strftime("%d.%m.%Y %H.%M.%S")
        Store.__store_instances.append((formatted_time, copy.deepcopy(self.__products)))

    def add_product(self, product: List[Product]):
        """Adds a new product to the store."""
        try:
            if isinstance(product, Product):
                self.__products.append(product)
            else:
                raise ValueError(ConstantStrings.PRODUCT_INVALID_TYPE)
        except ValueError as e:
            print(ConstantStrings.EXCEPTION_STRING.format(field="product", exception=e))

    def remove_product(self, product: List[Product]):
        """Removes a product from store."""
        try:
            if isinstance(product, Product):
                self.__products.remove(Product)
            else:
                raise ValueError(ConstantStrings.PRODUCT_INVALID_TYPE)
        except ValueError as e:
            print(ConstantStrings.EXCEPTION_STRING.format(field="product", exception=e))

    def get_total_quantity(self) -> int:
        """Returns how many items are in the store in total."""
        return sum((x.quantity for x in self.__products))

    def get_all_products(self) -> List[Product]:
        """Returns all products in the store that are active."""
        return [x for x in self.__products if x.active]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """
        Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order.
        :param shopping_list :List[Tuple[Product,int]]
        :return:  the total price of the order.
        """
        try:
            order_price = 0.0
            for item in shopping_list:
                if item[0] not in self.__products:
                    raise ValueError(ConstantStrings.
                                     STORE_PRODUCT_NOT_EXISTS.format(name=item[0].name))

                order_price += item[0].buy(item[1])
            return order_price
        except ValueError as e:
            print(ConstantStrings.EXCEPTION_STRING.format(field="order", exception=e))
            raise

    def __str__(self):
        """String representation of the Store."""
        return ConstantStrings.STORE_INFO.format(length=len(self.__products))
