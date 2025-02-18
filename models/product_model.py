"""The Product Model Module."""
import uuid
from constants.constant_strings import ConstantStrings


class ProductModel:
    """The Product Model Class."""

    def __init__(self, name, price, quantity):
        self.__id = None
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        """Product Name."""
        return self.__name

    @name.setter
    def name(self, value: str):
        try:
            if not isinstance(value, str) or not value.strip():
                raise ValueError(ConstantStrings.PRODUCT_NAME_ERROR)
            self.__name = value.strip()
        except ValueError as e:
            print(ConstantStrings.EXCEPTION_STRING.format(field="name", exception=e))
            raise  # re-raises the same exception

    @property
    def price(self):
        """Product Price."""
        return self.__price

    @price.setter
    def price(self, value: (int, float)):
        try:
            if not isinstance(value, (int, float)) or value < 0:
                raise ValueError(ConstantStrings.PRODUCT_PRICE_ERROR)
            self.__price = value
        except ValueError as e:
            print(ConstantStrings.EXCEPTION_STRING.format(field="price", exception=e))
            raise

    @property
    def quantity(self):
        """Product Quantity."""
        return self.__quantity

    @quantity.setter
    def quantity(self, value: (int, float)):
        try:
            if not isinstance(value, (int, float)) or value < 0:
                raise ValueError(ConstantStrings.PRODUCT_QUANTITY_ERROR)
            self.__quantity = value
        except ValueError as e:
            print(ConstantStrings.EXCEPTION_STRING.format(field="quantity", exception=e))
            raise

    @property
    def active(self):
        """Is Product Active."""
        return self.__quantity > 0

    @property
    def id(self):
        """Product Unique ID."""
        if not self.__id:
            self.__id: int = uuid.uuid4().int  # unique id to identify the product
        return self.__id

    def show(self) -> str:
        """The Product Info"""
        return f"{self.__name}, Price: ${self.__price}, Quantity: {self.__quantity}"

    def __str__(self):
        """The Product info object."""
        return (f"Product(name={self.__name}, "
                f"price={self.__price}, "
                f"quantity={self.__quantity}, "
                f"active={self.__active})")
