"""The Product Model Module."""
from constants import constant
import uuid


class ProductModel:
    """The Product Model Class."""

    def __init__(self, name, price, quantity):
        self.__name: str = name
        self.__price: float = price
        self.__quantity: int = quantity
        self.__active: bool = True
        self.__id: int = uuid.uuid4().int  # unique id to identify the product

    @property
    def name(self):
        """Product Name."""
        return self.__name

    @name.setter
    def name(self, value: str):
        try:
            if not isinstance(value, str) or not value.strip():
                raise ValueError(constant.PRODUCT_NAME_ERROR)
            self.__name = value.strip()
        except ValueError as e:
            print(constant.EXCEPTION_STRING.format(field="name", exception=e))
            raise  # re-raises the same exception

    @property
    def price(self):
        """Product Price."""
        return self.__price

    @price.setter
    def price(self, value: (int, float)):
        try:
            if not isinstance(value, (int, float)) or value < 0:
                raise ValueError(constant.PRODUCT_PRICE_ERROR)
            self.__price = value
        except ValueError as e:
            print(constant.EXCEPTION_STRING.format(field="price", exception=e))
            raise

    @property
    def quantity(self):
        """Product Quantity."""
        return self.__quantity

    @quantity.setter
    def quantity(self, value: (int, float)):
        try:
            if not isinstance(value, (int, float)) or value < 0:
                raise ValueError(constant.PRODUCT_QUANTITY_ERROR)
            self.__quantity = value
        except ValueError as e:
            print(constant.EXCEPTION_STRING.format(field="quantity", exception=e))
            raise

    @property
    def active(self):
        """Is Product Active."""
        return self.__active

    @active.setter
    def active(self, value: bool):
        """Is Product Active."""
        self.__active = value

    @property
    def id(self):
        """Product Unique ID."""
        return self.__id

    def __str__(self):
        """The Product info."""
        return f"Product(name={self.__name}, price={self.__price}, quantity={self.__quantity}, active={self.__active})"
