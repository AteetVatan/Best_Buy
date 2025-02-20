"""The Product Model Module."""
import uuid
from abc import ABC, abstractmethod
from helpers.product_validators import ProductValidators


class ProductModel(ABC, ProductValidators):
    """The Product Model Class."""

    # setup initial stock of inventory
    # product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
    #                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    #                 products.Product("Google Pixel 7", price=500, quantity=250),
    #                 products.NonStockedProduct("Windows License", price=125),
    #                 products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    #                 ]
    # best_buy = store.Store(product_list)

    def __init__(self, name, price, quantity=None, maximum=None):
        self.__active = None
        self.__name: str = None
        self.__price: (int, float) = None
        self.__quantity: (int, float) = None
        self.__maximum_order_quantity: (int, float) = None
        self.__active: bool = True  # By default, all products are active.
        self.__id = uuid.uuid4().int  # Unique product id
        self.name, self.price, self.quantity, self.maximum = name, price, quantity, maximum

    @abstractmethod
    def buy(self, buy_quantity: (int, float)):
        """Abstract method to buy product."""
        pass

    @abstractmethod
    def buy_validation(self, buy_quantity: (int, float)):
        """Abstract method to validate buy_quantity."""
        pass

    @property
    def name(self):
        """Product Name."""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Method to validate_and_set_name"""
        self.__name = ProductModel.validate_name(value)

    @property
    def price(self):
        """Product Price."""
        return self.__price

    @price.setter
    def price(self, value: (int, float)):
        """Method to validate_and_set_name"""
        self.__price = ProductModel.validate_price(value)

    @property
    def quantity(self):
        """Product Quantity."""
        return self.__quantity

    @quantity.setter
    def quantity(self, value: (int, float)):
        """Product Quantity."""
        if value is not None:
            self.__quantity = ProductModel.validate_quantity(value)

    @property
    def maximum(self):
        """Product Maximum Quantity."""
        return self.__maximum_order_quantity

    @maximum.setter
    def maximum(self, value: (int, float)):
        """Product Maximum Quantity."""
        if value is not None:
            self.__maximum_order_quantity = ProductModel.validate_quantity(value)

    @property
    def active(self):
        """Is Product Active."""
        return self.__active

    @active.setter
    def active(self, val: bool):
        """Sets Product Active."""
        self.__active = ProductModel.validate_active(val)

    @property
    def id(self):
        """Product Unique ID."""
        return self.__id

    def show(self) -> str:
        """The Product Info"""
        attributes = {
            "": self.__name,
            "Price: $": self.__price,
            "Quantity: ": self.__quantity,
            "Maximum: ": self.__maximum_order_quantity
        }
        return " ,".join(f"{k}{v}" for k, v in attributes.items() if v is not None)

    def __str__(self):
        """The Product info object."""
        """The Product info object."""
        attributes = {
            "name": self.__name,
            "price": self.__price,
            "quantity": self.__quantity,
            "active": self.__active,
            "maximum": self.__maximum_order_quantity
        }
        obj_str = " ,".join(f"{k}={v}" for k, v in attributes.items() if v is not None)
        return f"Product({obj_str})"
